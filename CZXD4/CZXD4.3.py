import tkinter as tk
import requests
import json

window = tk.Tk()

window.title('控制小钉4.3')

window.geometry('500x350')

l = tk.Label(window, text="欢迎使用控制小钉4.3,在绿色输入框里输入你想要发送的文字", bg='DarkBlue', fg='SpringGreen', font=('Arial', 12),
             width=100, height=2)
l.pack()

e = tk.Entry(window, show=None, width=100, bg="SeaGreen", fg='Thistle')
e.pack()

t = tk.Text(window, height=18, bg='Turquoise', fg='DarkGreen')
t.pack()


def send():
    var = e.get()
    url = "https://oapi.dingtalk.com/robot/send?access_token=fd70752caa12ac7be000218d355c2baa8d90ed79a0e2dbe2a5a87ab3ccf\
    540ff"
    text = (var + ".")
    if len(text) < 2:
        return 0
    program = {
        "isAtAll": "true",
        "msgtype": "text",
        "text": {"content": text},
    }
    headers = {'Content-Type': 'application/json'}
    f = requests.post(url, data=json.dumps(program), headers=headers)
    t.insert('end', ("已发送:   " + text + "\n"))


b1 = tk.Button(window, text='发送', width=60,
               height=2, bg='PaleTurquoise', fg='Navy', command=send)
b1.pack()

window.mainloop()
