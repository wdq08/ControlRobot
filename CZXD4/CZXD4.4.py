import tkinter as tk
import requests
import json
import time

window = tk.Tk()

window.title('控制小钉4.4')

window.geometry('500x400')

l = tk.Label(window, text="欢迎使用控制小钉4.4,在绿色输入框里输入你想要发送的文字", bg='DarkBlue', fg='SpringGreen', font=('Arial', 12),
             width=100, height=2)
l.pack()

e = tk.Entry(window, show=None, width=100, bg="SeaGreen", fg='Thistle')
e.pack()

t = tk.Text(window, height=18, bg='Turquoise', fg='DarkGreen')
t.pack()

number = 0


def send():
    var = e.get()
    url = "https://oapi.dingtalk.com/robot/send?access_token=fd70752caa12ac7be000218d355c2baa8d90ed79a0e2dbe2a5a87ab3ccf540ff"
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
    global number
    number += 1
    t.insert('end', ("已发送:   " + text + "\n"))


tk.Label(window, text='发送条数:', ).place(x=25, y=350)
canvas = tk.Canvas(window, width=380, height=45, bg="green")
canvas.place(x=80, y=350)

# 填充进度条
fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="red")
x = 500  # 未知变量，可更改
n = 380 / x  # 465是矩形填充满的次数
for i in range(16):
    n = n + 380 / x
    canvas.coords(fill_line, (0, 0, n, 60))
    window.update()
    time.sleep(0.02)  # 控制进度条流动的速度
if number % 20 == 0:
    # 清空进度条
    fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
    x = 500  # 未知变量，可更改
    n = 380 / x  # 465是矩形填充满的次数

    for t in range(x):
        n = n + 465 / x
        # 以矩形的长度作为变量值更新
        canvas.coords(fill_line, (0, 0, n, 60))
        window.update()
        if number % 20 == 0:
            time.sleep(0)  # 时间为0，即飞速清空进度条

b1 = tk.Button(window, text='发送', width=60,
               height=2, bg='PaleTurquoise', fg='Navy', command=send)
b1.pack()

window.mainloop()
