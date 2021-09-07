def split(string):
    return string.split(' ')

sentence = split(input("문장 하나를 입력하세요 : "))

for word in sentence:
    print(word.upper(), end="\n")


 