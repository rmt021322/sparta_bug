#연속한 1의 개수 중 최댓값
#01011010111 => 3 출력
T = int(input())
for testcase in range(1,T+1) :
    N = int(input())
    arr = list(map(int,input()))
    countone = 0
    maxone = float('-inf')

    for i in range(N):
        if arr[i] == 1 :#1이 나오면
            countone += 1 
        
        else : #arr[i] == 0
            if maxone <= countone : #현재 1 개수가 최댓값보다 크면
                maxone = countone #갱신
                countone = 0 #초기화

    if maxone <= countone:
        maxone = countone

    print(f'#{testcase} {maxone}')
