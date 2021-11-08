from tkinter import *

frame = Tk()
image = PhotoImage(file="GUI/Jupytor.PNG")
label1 = Label(frame, text="라벨입니다")
label1.pack()

label2 = Label(frame, image=image)
label2.pack()

frame.mainloop()
