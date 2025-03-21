
# i번 돌을 기준으로
# 마주보는 j개 돌
# 같은색이면 뒤집고 다른색이면 가만 두고
# 범위를 벗어나면 뒤집기 중지

T = int(input())  # 테스트케이스 개수
for test_case in range(1, T + 1):  # 테스트 케이스동안
    N, M = map(int, input().split())  # 돌 N개, 뒤집기 M회
    arr = list(map(int, input().split()))  # 돌 초기상태

    for a in range(M):  # 뒤집기 동안
        i, j = map(int, input().split())  # i번째 돌 기준 마주보는 j개
   

        # i번째 돌을 사이에 두고 마주보는 j개 돌
        i -= 1 #돌 번호가 1부터 시작하니가 인덱스로 바꾸는 -1 계산

        # 마주보는 돌이니까 i값 제외하면
        # 마주보는 돌의 쌍은 총 j개
        # j번 반복하면서 마주보는 돌의 상태 조건에 따라 바꾸기
        # 조건 : 마주보는 돌(i-k,i+k) 가 같으면 바꾸기
        for k in range(1,j+1):
            # 왼쪽이나 오른쪽이 인덱스의 범위를 벗어나면 중단
            if i-k < 0 or i+k >= N: #범위 N을 k가 넘어가지 않으면
                break

            
            # 마주보는 두 돌의 색이 같다면
            if arr[i-k] == arr[i+k]:
                if arr[i-k] ==0:  # 0이었으면 1로 바꾸고
                    arr[i-k] = arr[i+k] = 1
                else : # 그게 아니면 0으로 바꾸고
                    arr[i-k]=arr[i+k]=0
               
                
               
        
    
    # 돌 뒤집기 M번 후 돌의 상태 출력
    print(f"#{test_case}", *arr)




'''
강사님 풀이
# i는 1번부터 시작이므로 인덱스와 맞추기 위해 -1
        i -= 1

        # 마주보는 돌의 인덱스를 일단 계산해보면
        # i를 제외하고
        # (i-1, i+1) : 1개, (i-2, i+2) : 2개 ... (i-j, i+j) : j개
        # 마주보는 돌의 쌍은 총 j개
        # j번 반복하면서 마주보는 돌의 상태 조건에 따라 바꾸기
        # 조건 : 마주보는 돌(i-k,i+k) 가 같으면 바꾸기
        for k in range(1,j+1):
            # 왼쪽이나 오른쪽이 인덱스의 범위를 벗어나면 중단!
            if i-k < 0 or i+k >= N:
                break

            
            # 마주보는 두 돌의 색이 같다면
            if stones[i-k] == stones[i+k]:
                # 0이었으면 1로 바꾸고
                # 그게 아니면 0으로 바꾸고
                stones[i-k] = stones[i+k] = 1 if stones[i-k] == 0 else 0
        
    
    # 돌 뒤집기를 M번 하고 나서 돌의 상태 출력
    print(f"#{tc}", *stones)
'''

'''
풀이 1
#import sys
#sys.stdin = open("sample_in.txt", "r")

# i번 돌을 기준으로
# 마주보는 j개 돌
# 같은색이면 뒤집고 다른색이면 가만 두고
# 범위를 벗어나면 뒤집기 중지

T = int(input())  # 테스트케이스 개수
for test_case in range(1, T + 1):  # 테스트 케이스동안
    N, M = map(int, input().split())  # 돌 N개, 뒤집기 M회
    arr = list(map(int, input().split()))  # 돌 초기상태

    for a in range(M):  # 뒤집기 동안
        i, j = map(int, input().split())  # i번째 돌 기준 마주보는 j개
        # i번째 돌을 사이에 두고 마주보는 j개 돌

        for b in range(i - j, i + j):  # i를 마주보는 j범위에서_i는 제외
            # 같은색이면 뒤집고
            if arr[i + b] == arr[i - b ]:
                arr[b] = 1 - arr[b]
            # 다른 색이면 그대로 두고
            if arr[i + b] != arr[i - b]:
                pass

    print(f'#{test_case}', *arr)
'''



'''
17:10시점 풀이2
# i번 돌을 기준으로
# 마주보는 j개 돌
# 같은색이면 뒤집고 다른색이면 가만 두고
# 범위를 벗어나면 뒤집기 중지

T = int(input())  # 테스트케이스 개수
for test_case in range(1, T + 1):  # 테스트 케이스동안
    N, M = map(int, input().split())  # 돌 N개, 뒤집기 M회
    arr = list(map(int, input().split()))  # 돌 초기상태

    for a in range(M):  # 뒤집기 동안

        i, j = map(int, input().split())  # i번째 돌 기준 마주보는 j개
        # i번째 돌을 사이에 두고 마주보는 j개 돌

        right = i-j
        left = i+j+1
        mirror = 2*i +1

        for b in range(right, left):  # i를 마주보는 j범위에서_i는 제외
            # 같은색이면 뒤집고
            if arr[b] == arr[mirror]:
                arr[b] = 1 - arr[b]
            # 다른 색이면 그대로 두고
            if arr[b] != arr[mirror]:
                pass

    print(f&apos;#{test_case}&apos;, *arr)

'''
