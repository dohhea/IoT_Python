# 주사위 경기
# 주사위 놀이를 하는 프로그램을 작성합니다
# •
# 컴퓨터와 사용자가 하나씩의 주사위를 던지는데
# •
# 높은 눈이 나오는 쪽이 이기는 겁니다 . 같은 눈이 나오면 비
# 겼다는 메시지를 출력해 주면 됩니다
# •
# 게임을 계속할지 여부를 묻고 , 원하는 만큼 경기를 계속하도
# 록 합니다
# •
# 경기가 종료되면 그때까지의 승패정보를 출력해 줍니다

import random as rand
class Die:
    def __init__(self, max=6):
        self.MAX = max              # 만드는 주사위 면의 수
	
    # 주사위 던지기
    def roll(self):
        self.faceValue = int(rand.random()*self.MAX)+1
	
    def getFaceValue(self):
        return self.faceValue
	
    def toString(self):
        return str(self.faceValue)

def main():
    userWin= 0
    comWin = 0
    draw= 0
    user = Die()                        # 사용자의 주사위
    com = Die()		                    # 컴퓨터의 주사위

    # 게임의 진행
    while (True):
		# 게임 한번하고
        user.roll()
        com.roll()
        print("나는 : "+ user.toString() + ", 컴은 : " + com.toString())
        if (user.getFaceValue() == com.getFaceValue()):
            print("비겼습니다.")
            draw +=1
        elif (user.getFaceValue() > com.getFaceValue()):
            print("내가 이겼습니다.")
            userWin+=1
        else:
            print("컴이 이겼습니다.")
            comWin+=1
		
        # 계속 진행할지의 여부 파악
        cont=input("계속할까요? (y/n) ")
        if cont=="n" or cont=="N":
            break

    # 게임 총 결과 출력
    print ("총 "+ str(userWin + comWin + draw) + "경기 중 user " + str(userWin) + "회 승, COM "+ str(comWin) + "회 승, 무승부 " + str(draw) + "회" )


main()
