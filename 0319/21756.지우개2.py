N = int(input())  # 입력된 값
arr = [0] * (N + 1)  # 0값이 N개인 배열 만들기
new_arr = [0] * (N + 1)

for i in range(1, N + 1):  # 1부터 n+1칸까지 i값 저장
    arr[i] = i

# print(arr) #[0, 1, 2, 3, 4, 5]

j = 1
while len(new_arr) == 1:
    for a in range(1, N + 1):
        if a % 2 == 0:  # 인덱스 자릿수를 계산하는 방법
            new_arr[a] = arr[a]  # 이렇게?
            print(new_arr)
            j += 1
            '''
            [0, 0, 2, 0, 0, 0]
            [0, 0, 2, 0, 4, 0]
            '''
    final = []
    for b in range(N):
        if new_arr[a] != 0:
            final.append(new_arr[b])
    print(final)
