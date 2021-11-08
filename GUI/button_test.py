# 버튼과 핸들러 및 버튼의 text변경

from tkinter import *

def action():
    button.config(text="OK")                # 위젯의 속성은 config를 사용하여 변경가능

frame = Tk()
frame.title("버튼 연습")

button = Button(frame, command=action, text="Button")
button.pack()

frame.mainloop()
