# 문자열을 입력받아 공백을 구분자로 단어를 분리한 후 이를 모두 대문자로 바꾸어 출력
def split(string):
    return string.split(' ')

sentence = split(input("문장 하나를 입력하세요 : "))

for word in sentence:
    print(word.upper(), end="\n")


 