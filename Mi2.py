from bluepy import btle
import argparse
import os
import re
from dataclasses import dataclass
from collections import deque
import threading
import time
import signal
import traceback
import math
import logging
import json
import requests
import ssl

import sys
import bluetooth._bluetooth as bluez
# import cryptoFunctions
from bluetooth_utils import (toggle_device,
                             enable_le_scan, parse_le_advertising_events,
                             disable_le_scan, raw_packet_to_str)

readme = """

Please read README.md in this folder. Latest version is available at https://github.com/JsBergbau/MiTemperature2#readme
This file explains very detailed about the usage and covers everything you need to know as user.

"""


@dataclass
class Measurement:
    temperature: float
    humidity: int
    voltage: float
    calibratedHumidity: int = 0
    battery: int = 0
    timestamp: int = 0
    sensorname: str = ""
    rssi: int = 0

    def __eq__(self, other):  # rssi may be different, so exclude it from comparison
        if self.temperature == other.temperature and self.humidity == other.humidity and self.calibratedHumidity == other.calibratedHumidity and self.battery == other.battery and self.sensorname == other.sensorname:
            # in passive mode also exclude voltage as it changes often due to frequent measurements
            return True if args.passive else (self.voltage == other.voltage)
        else:
            return False


parser = argparse.ArgumentParser(allow_abbrev=False, epilog=readme)
parser.add_argument("--device", "-d", help="Set the device MAC-Address in format AA:BB:CC:DD:EE:FF",
                    metavar='AA:BB:CC:DD:EE:FF')
parser.add_argument("--battery", "-b",
                    help="Get estimated battery level, in passive mode: Get battery level from device", metavar='',
                    type=int, nargs='?', const=1)
parser.add_argument("--count", "-c", help="Read/Receive N measurements and then exit script", metavar='N', type=int)
parser.add_argument("--interface", "-i", help="Specifiy the interface number to use, e.g. 1 for hci1", metavar='N',
                    type=int, default=0)
parser.add_argument("--unreachable-count", "-urc", help="Exit after N unsuccessful connection tries", metavar='N',
                    type=int, default=0)
parser.add_argument("--mqttconfigfile", "-mcf", help="specify a configurationfile for MQTT-Broker")

passivegroup = parser.add_argument_group("Passive mode related arguments")

passivegroup.add_argument("--passive", "-p", "--atc", "-a",
                          help="Read the data of devices based on BLE advertisements, use --battery to get battery level additionaly in percent",
                          action='store_true')
passivegroup.add_argument("--watchdogtimer", "-wdt", metavar='X', type=int,
                          help="Re-enable scanning after not receiving any BLE packet after X seconds")
passivegroup.add_argument("--devicelistfile", "-df",
                          help="Specify a device list file giving further details to devices")
passivegroup.add_argument("--onlydevicelist", "-odl", help="Only read devices which are in the device list file",
                          action='store_true')
passivegroup.add_argument("--rssi", "-rs", help="Report RSSI via callback", action='store_true')

args = parser.parse_args()

advCounter = dict()

sensors = dict()
if args.devicelistfile:
    # import configparser
    if not os.path.exists(args.devicelistfile):
        print("Error: specified device list file '", args.devicelistfile, "' not found")
        os._exit(1)
    sensors = configparser.ConfigParser()
    sensors.read(args.devicelistfile)
    # Convert macs in devicelist file to Uppercase
    sensorsnew = {}
    for key in sensors:
        sensorsnew[key.upper()] = sensors[key]
    sensors = sensorsnew
    # loop through sensors to generate key
    sensorsnew = sensors
    for sensor in sensors:
        if "decryption" in sensors[sensor]:
            if sensors[sensor]["decryption"][0] == "k":
                sensorsnew[sensor]["key"] = sensors[sensor]["decryption"][1:]
            # print(sensorsnew[sensor]["key"])
    sensors = sensorsnew

import configparser


# import paho.mqtt.client as mqtt

# mqttConfig = configparser.ConfigParser()

# MQTTTopic = mqttConfig["MQTT"]["topic"]


def decode_data_atc(mac, adv_type, data_str, rssi, measurement):
    preeamble = "161a18"
    packetStart = data_str.find(preeamble)
    offset = packetStart + len(preeamble)
    strippedData_str = data_str[offset:offset + 26]  # if shorter will just be shorter then 13 Bytes
    strippedData_str = data_str[offset:]  # if shorter will just be shorter then 13 Bytes
    macStr = mac.replace(":", "").upper()
    dataIdentifier = data_str[(offset - 4):offset].upper()

    batteryVoltage = None

    if (dataIdentifier == "1A18") and not args.onlydevicelist or (dataIdentifier == "1A18" and mac in sensors) and (
            len(strippedData_str) in (16, 22, 26, 30)):  # only Data from ATC devices
        if len(strippedData_str) == 30:  # custom format, next-to-last ist adv number
            advNumber = strippedData_str[-4:-2]
        else:
            advNumber = strippedData_str[-2:]  # last data in packet is adv number
        if macStr in advCounter:
            lastAdvNumber = advCounter[macStr]
        else:
            lastAdvNumber = None
        if lastAdvNumber == None or lastAdvNumber != advNumber:

            if len(strippedData_str) == 26:  # ATC1441 Format
                print("BLE packet - ATC1441: %s %02x %s %d" % (mac, adv_type, data_str, rssi))
                advCounter[macStr] = advNumber
                # temperature = int(data_str[12:16],16) / 10.    # this method fails for negative temperatures
                temperature = int.from_bytes(bytearray.fromhex(strippedData_str[12:16]), byteorder='big',
                                             signed=True) / 10.
                humidity = int(strippedData_str[16:18], 16)
                batteryVoltage = int(strippedData_str[20:24], 16) / 1000
                batteryPercent = int(strippedData_str[18:20], 16)

            elif len(strippedData_str) == 30:  # Custom format
                print("BLE packet - Custom: %s %02x %s %d" % (mac, adv_type, data_str, rssi))
                advCounter[macStr] = advNumber
                temperature = int.from_bytes(bytearray.fromhex(strippedData_str[12:16]), byteorder='little',
                                             signed=True) / 100.
                humidity = int.from_bytes(bytearray.fromhex(strippedData_str[16:20]), byteorder='little',
                                          signed=False) / 100.
                batteryVoltage = int.from_bytes(bytearray.fromhex(strippedData_str[20:24]), byteorder='little',
                                                signed=False) / 1000.
                batteryPercent = int.from_bytes(bytearray.fromhex(strippedData_str[24:26]), byteorder='little',
                                                signed=False)

            elif len(strippedData_str) == 22 or len(
                    strippedData_str) == 16:  # encrypted: length 22/11 Bytes on custom format, 16/8 Bytes on ATC1441 Format
                if macStr in advCounter:
                    lastData = advCounter[macStr]
                else:
                    lastData = None

                if lastData == None or lastData != strippedData_str:
                    print("BLE packet - Encrypted: %s %02x %s %d, length: %d" % (
                    mac, adv_type, data_str, rssi, len(strippedData_str) / 2))
                    advCounter[macStr] = strippedData_str
                    if mac in sensors and "key" in sensors[mac]:
                        bindkey = bytes.fromhex(sensors[mac]["key"])
                        macReversed = ""
                        for x in range(-1, -len(macStr), -2):
                            macReversed += macStr[x - 1] + macStr[x]
                        macReversed = bytes.fromhex(macReversed.lower())
                        # print("New encrypted format, MAC:" , macStr, "Reversed: ", macReversed)
                        lengthHex = data_str[offset - 8:offset - 6]
                        # lengthHex="0b"
                        ret = cryptoFunctions.decrypt_aes_ccm(bindkey, macReversed,
                                                              bytes.fromhex(lengthHex + "161a18" + strippedData_str))
                        if ret == None:  # Error decrypting
                            print("\n")
                            return
                        # temperature, humidity, batteryPercent = cryptoFunctions.decrypt_aes_ccm(bindkey,macReversed,bytes.fromhex(lengthHex + "161a18" + strippedData_str))
                        temperature, humidity, batteryPercent = ret
                    else:
                        print("Warning: No key provided for sensor:", mac, "\n")
                        return
                else:
                    return  # repeated packet
            else:  # no fitting packet
                return

        else:  # Packet is just repeated
            return

        measurement.battery = batteryPercent
        measurement.humidity = humidity
        measurement.temperature = temperature
        measurement.voltage = batteryVoltage if batteryVoltage != None else 0
        measurement.rssi = rssi
        return measurement


def decode_data_qingping(mac, adv_type, data_str, rssi, measurement):
    preeamble = "cdfd88"
    packetStart = data_str.find(preeamble)
    offset = packetStart + len(preeamble)
    strippedData_str = data_str[offset:offset + 32]
    macStr = mac.replace(":", "").upper()
    dataIdentifier = data_str[(offset - 2):offset].upper()

    if (dataIdentifier == "88") and not args.onlydevicelist or (dataIdentifier == "88" and mac in sensors) and len(
            strippedData_str) == 32:
        print("BLE packet - Qingping: %s %02x %s %d" % (mac, adv_type, data_str, rssi))
        temperature = int.from_bytes(bytearray.fromhex(strippedData_str[18:22]), byteorder='little', signed=True) / 10.
        humidity = int.from_bytes(bytearray.fromhex(strippedData_str[22:26]), byteorder='little', signed=True) / 10.
        batteryPercent = int(strippedData_str[30:32], 16)

        measurement.battery = batteryPercent
        measurement.humidity = humidity
        measurement.temperature = temperature
        measurement.rssi = rssi
        return measurement


def le_advertise_packet_handler(mac, adv_type, data, rssi):
    global lastBLEPacketReceived
    if args.watchdogtimer:
        lastBLEPacketReceived = time.time()
    lastBLEPacketReceived = time.time()
    data_str = raw_packet_to_str(data)

    global measurements
    measurement = Measurement(0, 0, 0, 0, 0, 0, 0, 0)
    measurement = (
            decode_data_atc(mac, adv_type, data_str, rssi, measurement)
            or
            decode_data_qingping(mac, adv_type, data_str, rssi, measurement)
    )

    if measurement:
        # if args.influxdb == 1:
        measurement.timestamp = int((time.time() // 10) * 10)
        # measurement.timestamp = int((time.time() // 10) * 10)
        # else:
        #	measurement.timestamp = int(time.time())

        # if args.round:
        if True:
            measurement.temperature = round(measurement.temperature, 1)
            measurement.humidity = round(measurement.humidity, 1)

        if mac in sensors and "sensorname" in sensors[mac]:
            print("传感器名字:", sensors[mac]["sensorname"])

        print("温度: ", measurement.temperature)
        print("湿度: ", measurement.humidity)
        if measurement.voltage != None:
            print("电池电压:", measurement.voltage, "V")
        print("RSSI:", rssi, "dBm")
        print("剩余电量:", measurement.battery, "%")

        print("采集结束了！")

    # currentMQTTTopic = MQTTTopic


dev_id = args.interface
toggle_device(dev_id, True)

sock = bluez.hci_open_dev(dev_id)

enable_le_scan(sock, filter_duplicates=False)

parse_le_advertising_events(sock, handler=le_advertise_packet_handler, debug=False)




