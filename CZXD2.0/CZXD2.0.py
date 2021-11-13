import requests
import json

while True:
    url = "https://oapi.dingtalk.com/robot/send?access_token=fd70752caa12ac7be000218d355c2baa8d90ed79a0e2dbe2a5a87ab3ccf540ff"
    text = (input() + ".")
    if text == "/exit.":
        exit(0)
    if len(text) < 2:
        continue
    program = {
        "isAtAll": "true",
        "msgtype": "text",
        "text": {"content": text},
    }
    headers = {'Content-Type': 'application/json'}
    f = requests.post(url, data=json.dumps(program), headers=headers)
