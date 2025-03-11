import sys
sys.stdin = open("input.txt", "r")


T = int(input()) #테스트케이스

for test_case in range(1,T+1):
    arr = [list(map(int,input().split())) for i in range(9)]
    print(arr)
    N = len(arr)
    print(N)

    #이동하면서 확인
    for i in range(1, 10) :
    #가로 세로 1부터 9까지 숫자 한번씩
    

    # arr(i,j) 위치에서
        # 가로로 확인
        # 세로로 확인
        #3*3 작은 격자에서 1부터 9까지 숫자 한번씩

    #겹치는 숫자가 없으면 1 출력
    #아니면 0 출력


