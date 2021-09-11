# 문자열을 입력받아 알파벳인경우 대문자->소문자 소문자->대문자 변경하여 출력
# 몇개의 문자가 변경되었는지도 출력
count=0

def toggle(ch):
    global count
    if (ch.isalpha()):
        count +=1
        if (ch>='a' and ch<='z'):
            return ch.upper()
        else:
            return ch.lower()
    return ch

string = input("문장 하나를 입력하세요 : ")

new_string = ""
for ch in string:
    new_string += toggle(ch)

print("Original string : " + new_string)
print("Changed string : " + new_string)
print("number of changes : ", count)

        