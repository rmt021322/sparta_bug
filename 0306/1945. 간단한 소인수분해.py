T = int(input())

arr = [2,3,5,7,11] #소인수 목록

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    count = [0]*5#케이스마다 초기화
    for i in range(5):
        while N % arr[i] == 0 :#나머지가 0일 때
            count[i] += 1 #횟수 증가 => 답
            N = N // arr[i] #몫 갱신
            
    print(f'#{test_case}', *count) #count 언패킹
