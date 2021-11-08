# 버튼과 핸들러 및 버튼의 text변경
# 중요한 것은 pack을 객체생성하면서 하면 Widget의 속성을 변경해 줄 때 에러가 남
# 따라서 분리해서 배치관리자를 사용함

from tkinter import *  
frame=Tk()

def doit():
    button.config(text=entry.get())         # entry의 값으로 버튼을 설정

label=Label(frame, text="이름")
label.pack()
entry=Entry(frame)
entry.pack()
button = Button(frame, command=doit, text="Button")
button.pack()

frame.mainloop()
