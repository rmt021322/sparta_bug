T = int(input()) #테스트케이스
N = int(input())#농장 크기
arr = [list(map(int, input().split())) for j in range(5)] #농장의 농작물 가치
#print(arr)
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    
    #마름모 만들기
    
    #마름모에 해당하는 범위값 읽기
