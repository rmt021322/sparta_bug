'''
import sys
sys.stdin = open("sample_in.txt", "r")
'''
T = int(input())
for testcase in range(1, T + 1):
    N, M = map(int, input().split())  # N개 돌 M회 뒤집기
    arr = list(map(int, input().split()))  # 돌 초기 상태
    # print(arr)
    # M회 뒤집기
    for a in range(M):  # 뒤집기 횟수
        i, j = map(int, input().split())  # 기준값i와 뒤집을 범위 i부터 j값
        #print(i)
        '''
        #i번째부터 j개 돌을 i번째 돌 색으로 뒤집기
        for b in range(i,j-1) :#i-1값부터 j번째 돌
            if 0 < i + j < N:  # N개 범위 내에 해당하는 값만
                arr[b] = arr[i] #b번째 돌을 i번째 돌값으로 바꾸기
        '''
        i-=1 #범위 

        for b in range(i+1, j+i):  # i번째값부터 j개 범위의 b값이
            if b < N: #N개 범위 안에 있으면
                arr[b] = arr[i]  # b번째 값을 i번째 arr값으로 변경

    print(f'#{testcase}', *arr)
