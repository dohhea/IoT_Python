# 매우 간단한 GUI 프로그램 샘플

from tkinter import *
from tkinter.ttk import *
import tkinter											# tkinter.CURRENT를 사용하기 위해 별로도 import 하여야 함

class MyFrame(Frame):									# 간단한 상속 활용

	def __init__(self, master):								# 생성자
		Frame.__init__(self, master)						# 상속받은 프레임을 master 로 연결

		self.buttonSave = Button()							# 나중에 쓰일 버튼을 정의해 주고
		def onClick():										# 이것이 눌릴때 실행할 핸들러를 정의
			str1=entryName.get()							
			str2=entryComp.get()
			txtComment.insert(tkinter.CURRENT, str1+str2)	# 두개의 Entry의 값을 Text에 출력함
			btnSave.configure(text="OK")

		self.master = master
		self.master.title("고객 입력")						# 프레임의 타이틀 설정
		self.pack(fill=BOTH, expand=True)					# 프레임의 속성 설정				

		# 성명
		frame1 = Frame(self)								# 상위 프레임에 들어갈 서브 프레임생성
		frame1.pack(fill=X)								# 수평방향으로 채워짐

		lblName = Label(frame1, text="성명", width=10)		# 레이블 1개
		lblName.pack(side=LEFT, padx=10, pady=10)

		entryName = Entry(frame1)						# 엔트리 1 개
		entryName.pack(fill=X, padx=10, expand=True)	

		# 회사
		frame2 = Frame(self)
		frame2.pack(fill=X)

		lblComp = Label(frame2, text="회사명", width=10)
		lblComp.pack(side=LEFT, padx=10, pady=10)

		entryComp = Entry(frame2)
		entryComp.pack(fill=X, padx=10, expand=True)

		# 특징
		frame3 = Frame(self)
		frame3.pack(fill=BOTH, expand=True)

		lblComment = Label(frame3, text="특징", width=10)
		lblComment.pack(side=LEFT, anchor=N, padx=10, pady=10)

		txtComment = Text(frame3)
		txtComment.pack(fill=X, pady=10, padx=10)

		# 저장
		frame4 = Frame(self)
		frame4.pack(fill=X)
		btnSave = Button(frame4, text="저장", command=onClick)	# 버튼을 생성하면서 핸들러를 위에 정의 한 onClick으로 설정
		btnSave.pack(side=LEFT, padx=10, pady=10)

def main():
    root = Tk()
    root.geometry("600x550+100+100")							# 프레임의 크기와 위치설정
    app = MyFrame(root)										# 프레임 생성
    root.mainloop()											# 프레임이 화면에 머물도록 함
 
 
if __name__ == '__main__':
    main()
