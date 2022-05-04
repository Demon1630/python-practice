import requests
#使用企业微信机器人

# url = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=633a31f6-7f9c-4bc4-97a0-0ec1eefa589"
url = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=8a9bcc0d-d81f-41d6-bd57-61d247f39976"
headers = {"Content-Type": "text/plain"}
s = "老婆子爱你！ "
data = {
      "msgtype": "text",
      "text": {
         "content": s,
      }
   }
r = requests.post(url, headers=headers, json=data)
print(r.text)
