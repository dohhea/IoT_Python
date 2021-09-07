def palindrome(str1):
    reverse_str=""
    for ch in str1:
        reverse_str=ch+reverse_str
    return str1==reverse_str

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
