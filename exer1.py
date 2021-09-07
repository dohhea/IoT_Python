sum=0

print(("10개의 수를 입력하세요 : "), end='\n')
for i in range(10):
    sum += int(input())

print("10개 수의 합은 : ", sum, end='\n')
print("10개 수의 평균은 : ", sum/10, end='\n')