# 섭씨 온도를 화씨온도로 바꾸는 예제
# 만약 입력에 이상이 있는 것이 들어오면 exception을 처리하도록 함

from tkinter import *  
frame=Tk()

def doit():
    label4.config(text="")                                      # 에러메시지 라벨 초기화
    try:
        label3.config(text=(eval(entry.get() + "*9/5 + 32")))   # 화씨온도로 변환
    except:
        label4.config(text="입력값 이상. 다시입력.")              # 에러메시지 출력

label1=Label(frame, text="섭씨온도")
label1.grid(row=0, column=0)
entry=Entry(frame)
entry.grid(row=0, column=1)
label2=Label(frame, text="화씨온도")
label2.grid(row=1, column=0)
label3=Label(frame, text="")
label3.grid(row=1, column=1)

button = Button(frame, command=doit, text="온도변환")
button.grid(row=2, column=0, columnspan=2)
label4=Label(frame, text="")
label4.grid(row=3, column=0, columnspan=2)

frame.mainloop()
