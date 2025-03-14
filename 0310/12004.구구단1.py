
#import sys
#sys.stdin = open("input.txt", "r")

TC = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, TC + 1):
    N = int(input())
    #주어진 정수 N이 1이상 9 이하의 두 수 a,b의 곱으로 표현될 수 있을까
    #표현되면 yes 아니면 no
    answer = "No" # 기본값 no로 설정
    
    #a*b가 N일때 yes를 출력하자
    #숫자범위 1<= N <= 9
    for a in range(1,10) : #1이상 10미만
        for b in range(1,10):
            if a*b == N:#a, b의 곱이 N일때
                answer = "Yes" #yes출력
                
        if answer == "Yes": #yes가 출력되었으면 반복 종료
            break


    print(f'#{test_case} {answer}')
