#n이 주어질 때 1부터 n까지의 합

n = int(input()) #n 입력
fac = 0 #합 결과 입력 초깃값
for i in range(1,n+1): #1부터 n까지 더하기
    fac += i #fac에 저장
print(fac) #출력
