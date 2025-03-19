'''
N개의 칸 1부터 N까지 수가 왼쪽부터 순서대로 저장
처음 각 칸 번호와 각 칸 저장된 수가 같다

idx 1234
값  1234

정확히 하나가 남을 때까지 아래 작업 반복
1) 홀수번 칸의 수 모두 지우기
2) 남은 수 왼쪽으로 모으기

숫자가 적힌 칸이 하나 남으면
마지막 남은 숫자 하나 출력

'''

'''
N = int(input())  # 입력된 값
arr = [0] * N  # 0값이 N개인 배열 만들기
for i in range(1, N + 1):  # 1부터 n+1칸까지 i값 저장
    arr[i] = i

# 정확히 하나 남을 때까지 아래 작업 반복
for a in range(1, N + 1):
    # 홀수번 칸 수 모두 지우기
    if arr[a] % 2 == 1:
        arr[a] = None
    # 남은 수 왼쪽으로 모으기
    if arr[a] = None :  # arr i번째 값이 None이면
        arr[a], arr[i + 1] = arr[i + 1], arr[i]  # 오른쪽 값과 자리 바꾸기
    # arr 값이 하나 남으면
    if len(arr) == 1:
        print(arr[0])

    # 마지막 남은 숫자 하나 출력
'''

'''

N = int(input())  # 입력된 값
arr = [0]*(N+1)  # 0값이 N개인 배열 만들기
new_arr = []
for i in range(1, N + 1):  # 1부터 n+1칸까지 i값 저장
    arr[i] = i

#정확히 하나 남을 때까지 아래 작업 반복
while len(new_arr) < 1 :
    for a in range(1, N+1) :
    #지우개로 홀수번 칸 수들을 모두 지움
    #남은 수를 왼쪽으로 모음
    # => 리스트 새로 만들어서 남아야하는 원소만 추가
        # => 짝수번 칸들만 모아서 새 리스트 만듦
        if arr[a] % 2 == 0:
            new_arr += arr[a] #IndexError: list assignment index out of range
 


    #위 과정을 반복해 숫자가 1개 남으면 중단
     # => 새 리스트 길이가 1이면 출력
    answer = len(new_arr)
    print(answer)
'''

N = int(input())  # 입력된 값
arr = [0] * (N + 1)  # 0값이 N개인 배열 만들기
new_arr = []
for i in range(1, N + 1):  # 1부터 n+1칸까지 i값 저장
    arr[i] = i

# 정확히 하나 남을 때까지 아래 작업 반복
while len(new_arr) < 1:
    # 지우개로 홀수번 칸 수들을 모두 지움
    # 남은 수를 왼쪽으로 모음
    # => 리스트 새로 만들어서 남아야하는 원소만 추가
    # => 짝수번 칸들만 모아서 새 리스트 만듦
    for a in range(1, N + 1):
        if a % 2 == 0:  # 인덱스 자릿수를 계산하는 방법
            # b를 인덱스값으로 인식하고 계산하기
            # 어떻게???
            new_arr += arr[a]  # 이렇게?
            #IndexError: list index out of range

    # 위 과정을 반복해 숫자가 1개 남으면 중단
    # => 새 리스트 길이가 1이면 출력
answer = len(new_arr)
print(answer)

