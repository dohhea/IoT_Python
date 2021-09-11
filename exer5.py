# 입력된 문자열이 Palindrome인지 아닌지를 파악하여 출력
# gadget이라는 모듀을 만들고 거기에 palindrome 함수를 기술

from gadget import palindrome
def main():
    while(True):
        string = input("문자열 하나 입력하세요 : ")
        if string=="":
            print("Bye bye!")
            break
        if palindrome(string):
            print(string + " is a palindrome!")
        else:
            print(string + " is not a palindrome!")

main()
