import requests
import json

print("你好")
print("欢迎使用控制小钉3.1")
print("使用方法如下:")
print("输入你想要发送的文字然后按下回车即可发送")

while True:
    print("请输入: > ", end='>')
    url = "https://oapi.dingtalk.com/robot/send?access_token=fd70752caa12ac7be000218d355c2baa8d90ed79a0e2dbe2a5a87ab3ccf540ff"
    text = (input() + ".")
    if text == "/exit":
        break
    if len(text) < 2:
        continue
    program = {
        "isAtAll": "true",
        "msgtype": "text",
        "text": {"content": text},
    }
    headers = {'Content-Type': 'application/json'}
    f = requests.post(url, data=json.dumps(program), headers=headers)
