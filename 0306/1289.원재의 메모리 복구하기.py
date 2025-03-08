
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    memory = list(map(int, input()))#메모리 원래 값
    count = 0 #초기상태(모든bit 0)부터 원래 값까지 수정 횟수 
    status = [0]*len(memory) #초기 상태  
    N = len(memory)

    #i번째 숫자를 바꾸면 n째까지 숫자도 변경
    #최소 횟수 -> 필요할때만 변경하자
    for i in range(N):
        if memory[i] != status[i] :#원래값과 초기상태가 다르면
            for j in range(i,N): #I부터 끝까지
                status[i] = memory[i] #변경할 memory값으로 바뀌고
                count+=1 #변경횟수도 증가하고
            
                        
    print(f'#{test_case} {count}')



'''
#1 1 #2 1 #3 1
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    memory = list(map(int, input()))#메모리 원래 값
    count = 0 #초기상태(모든bit 0)부터 원래 값까지 수정 횟수 
    status = [0]*len(memory) #초기 상태  
    N = len(memory)

    #i번째 숫자를 바꾸면 n째까지 숫자도 변경
    #최소 횟수 -> 필요할때만 변경하자
    for i in range(N):
        if memory[i] != status[i] :#원래값과 초기상태가 다르면
            for j in range(i,N): #i번째부터 N값까지
                count+=1 # 변환 횟수 증가하고
                if memory[i] == 1: #원래값이 1이면
                    status[j] = 1 #초기값도 1
                else:#원래값 0이면
                    status[i] = 0 #초기값도 0

                        
        print(f'#{test_case} {count}')


#1 0 #2 0 #3 0

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    memory = list(map(int, input()))#메모리 원래 값
    count = 0 #초기상태(모든bit 0)부터 원래 값까지 수정 횟수 
    status = [0]*len(memory) #초기 상태  
    N = len(memory)

    #i번째 숫자를 바꾸면 n째까지 숫자도 변경
    #최소 횟수 -> 필요할때만 변경하자
    for i in range(N):
        while memory[i] == status[i] :#원래값과 초기상태가 같아질때까지
                if memory[i] == 1: #원래값이 1이면
                    for i in range(i,N,N-i+1): #i부터 N까지 N-i+1개가
                        status[i] = 1 #초기값도 1
                else:#원래값이  0이면
                    for j in range(j,N,N-j+1):
                    status[j] = 0 #초기값도 0
       print(f'#{test_case} {count}')
       '''
