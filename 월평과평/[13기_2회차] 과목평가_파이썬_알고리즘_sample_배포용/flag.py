'''
import sys
sys.stdin = open("algo_sample_in.txt", "r")
'''
T = int(input())
for testcase in range(1, T + 1):
    N, M = map(int, input().split())  # N개 돌 M회 뒤집기
    arr = list(map(int, input().split()))  # N명 초기상태
    # print(arr)
    # M회 뒤집기
    for i in range(M):  # 뒤집기 횟수
        a, b, c = map(int, input().split())  # a난이도, b 기준번호, c 비교범위
        #print(i)

        i-=1 #범위 

        for j in range(b+1, b+c):  # i번째값부터 j개 범위의 b값이
            if j < N: #N개 범위 안에 있으면
                arr[b] = arr[i]  # b번째 값을 i번째 arr값으로 변경
                arr

    print(f'#{testcase}', *arr)