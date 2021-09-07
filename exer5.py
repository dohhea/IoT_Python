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
