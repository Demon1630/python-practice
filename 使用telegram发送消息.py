import telegram

chat_id = '@Python1633'
token = '1779618476:AAHfqFU_KumuNdywCle3y-ZJCXa56SulYY8'
bot = telegram.Bot(token=token)

bot.send_message(chat_id=chat_id,text='测试')