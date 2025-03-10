
T = int(input())

for testcase in range(1,T+1):
    N, M = map(int, input().split()) #N개 돌 M회 뒤집기
    arr = list(map(int, input().split())) #돌 초기 상태
    #print(arr)

    #M회 뒤집기
    for a in range(1,M+1): #뒤집기 횟수
        i, j = map(int, input().split())  # 기준값i와 뒤집을 범위 i부터 j값
        #i번째부터 j개 돌을 i번째 돌 색으로 뒤집기
        for b in range(i,j) :
              #N개 범위 내에 해당하는 값만
                arr[b] = arr[i] #b번째 돌을 i번째 돌값으로 바꾸기

    print(f'#{testcase}', *arr)
