#평균값 출력하기
T = int(input()) 
 
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1,T+1):
     
    number = list(map(int,input().split()))
    first_sum = sum(number) #number합
    plus=sum(number)/10 #나눗셈
    #print(plus)
    plus_second= sum(number)//10 #정수나눗셈
     
    a = plus - plus_second #소수값 구해서
    #소수값 반올림
    if a > 0.4: #소수값이 0.5 이상이면
        plus_second += 1 #정수값 +1
    else: #아니면 원래 값 출력
        pass
 
   
    print(f'#{test_case} {plus_second}')
