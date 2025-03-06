T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M = map(int, input().split()) #숫자열 길이_ Ai N Bj M
    Ai = list(map(int,input().split())) #Ai 입력받기
    #print(Ai)
    Bj = list(map(int,input().split())) #Bi입력받기
    # 둘 중에 길이 긴 값을 Ai, 짧은 값을 Bj로 위치 변경
    if len(Ai) < len(Bj)  : #Ai가 Bj보다 작으면
        N, M = M, N #숫자열 길이 위치 변경
        long_arr = Bj
        short_arr = Ai
    else :
        long_arr = Ai
        short_arr = Bj
'''
    else :
    
        Ai, Bj = Ai, Bj #아니면 그대로
        #굳이 돌릴 필요 X

    #Ai 길이 맞춰서 새 배열 만들기
  
'''


    #최댓값 찾는 반복문
    max_sum = float('-inf') #음의무한대
    for i in  range(N-M+1) :#M이 이동하면서 N범위를 넘지 않는 범위
        facesum = 0 #마주보는 원소들 곱의 합
        for j in range(M):
            facesum += long_arr[i + j] * short_arr[j]  #마주보는 수 곱해서 더하기
        
        if max_sum < facesum : #최댓값이 facesum보다 작으면
            max_sum = facesum #facesum을 최댓값으로
            
    
    print(max_sum) #최댓값 출력         

'''


    내꺼만들기
    float('-inf') #음의 무한대
    0보다 활용성 좋음
    
    
'''
