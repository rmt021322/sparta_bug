T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    Ai = list(map(int,input().split()))
    #print(Ai)
    Bj = list(map(int,input().split()))
    #print(Ai)
    # 둘 중에 길이 긴 값을 Ai, 짧은 값을 Bj로 위치 변경
    if len(Ai) < len(Bj)  : #Ai가 Bj보다 작으면
        Ai, Bj = Bj, Ai #위치 변경
    else :
        Ai, Bj = Ai, Bj #아니면 그대로
        
    #Ai 길이 맞춰서 새 배열 만들기
    
    #새 배열 길이 내에서 Bi 위치 이동시키기
    
    #최댓값 찾는 반복문
        
