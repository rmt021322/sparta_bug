#1 min/max 내장함수 사용하기
#n개의 정수 중 최솟값 최댓값 구하기
N = int(input())
arr = list(map(int,input().split()))

print(f'{min(arr)} {max(arr)}')



#2. 반복문 사용하기
#n개의 정수 중 최솟값 최댓값 구하기
N = int(input()) #정수 N개
arr = list(map(int,input().split()))
min_arr = float('inf') #최댓값 저장_아주 큰값 대입
max_arr = float('-inf') #최솟값 저장_아주 작은값 대입


for i in range(N):
    if arr[i] >= max_arr: #i번째 arr값이 max_arr보다 크면
        max_arr = arr[i] #max_arr값에 최댓값 저장
    if arr[i] <= min_arr: #i번째 arr값이 min_arr보다 작으면
        min_arr = arr[i] #최솟값 저장

print(f'{min_arr} {max_arr}')

print(f'#{min_arr} {max_arr}')
