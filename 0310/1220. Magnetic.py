'''
목표 : 교착상태 개수 세기
A : 붉은 자성체는 S극에 이끌려 테이블 아래로
B : 푸른 자성체는 N극에 이끌려 테이블 아래로
C, D :좌우로 인접하면 다른 교착상태로 인정->개수 2개 판정
D처럼 셋 이상 자성체가 붙어있으면 교착상태 하나로 인정
E처럼 한 줄에 2개 이상 교착상태 가능


###
#함수정의하는 방법도 풀어보기
#교착상태 조건
def check_deadlock():
    #위아래로 1과 2가 맞닿을 때_서로 다른 방향을 보는 자성체가 맞닿을 때
    #서로 다른 방향을 보는 자성체가 좌우로 맞닿을 때 => 개수 2개 판정
    #셋 이상 자성체가 붙어있는 경우 1개 취급
'''    

T = 10 #테스트케이스 10개
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input()) #배열 한 변 길이
    arr = [list(map(int, input().split())) for _ in range(N)]
    #print(arr)
    
    count = 0 #교착상태 개수

    #1 = N극 자성체
    #2 = S극 자성체
    #테이블 윗부분이 N극 아래 S극
    #행우선 교착상태 찾기_행값 고정 열값 이동
    for i in range(N):
        for j in range(N-1):
            if arr[i][j] == 1 and arr[i][j+1]==2 : #현재값이 N극이고 다음값이 s극
                count += 1
            elif arr[i][j] ==2 and arr[i][j+1] ==1 : #현재값이 s극이고 다음값이 n극
                count += 1
    #열우선 교착상태 찾기
    for j in range(N):
        for i in range(N-1):
            if arr[i][j] == 1 and arr[i+1][j] == 2 : #현재값이 n극이고 다음값이 s극
                count += 1
            elif arr[j][i] == 2 and arr[i+1][j] ==1 :#현재값이 s극이고 다음값이 n극
                count += 1

    print(f'#{test_case} {count}') # #1 396 #2 401 ...
