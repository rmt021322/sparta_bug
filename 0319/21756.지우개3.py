N = int(input())  # 입력된 값
arr = [0] * (N + 1)  # 0값이 N개인 배열 만들기
new_arr = []

for i in range(1, N + 1):  # 1부터 n+1칸까지 i값 저장
    arr[i] = i

print(arr) #[0, 1, 2, 3, 4, 5]


while len(new_arr) > 1:
    for j in range(1, N + 1):  # 1부터 N까지 반복
        if j % 2 == 0:  # 짝수 인덱스일 때
            new_arr.append(arr[j])

    print(*new_arr)  # new_arr 출력
