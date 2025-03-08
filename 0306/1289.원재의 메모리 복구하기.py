
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    memory = list(map(int, input().split()))#메모리 원래 값
    count = 0 #초기상태(모든bit 0)부터 원래 값까지 수정 횟수 
    status = [0]*len(memory) #초기 상태  
    N = len(memory)

    #i번째 숫자를 바꾸면 n째까지 숫자도 변경
    #최소 횟수 -> 필요할때만 변경하자
    for i in range(N):
        if memory[i] != status[i] :#원래값과 초기상태가 다르면
            for j in range(i,N): #i번째부터 N값까지
                count+=1 # 변환 횟수 증가하고
                if memory[i] = 1: #원래값이 1이면
                    status[j] = 1 #초기값도 1
                else:#원래값 0이면
                    status[i] = 0 #초기값도 0

                        
        print(f'#{test_case} {count}')
