T = int(input())
#print(arr)
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
N = int(input()) #농장 크기
for test_case in range(1, T + 1):
    arr = [list(map(int, input().split())) for j in range(N)] #농장의 농작물 가치
    
    #마름모 만들기
    #정중앙점 기준으로 행 N칸에서 시작해서
    middle = N//2
    start = [middle,middle] #시작점 중앙값
    sum = 0 #총합 초깃값
    #위아래 한층씩 갈수록 행 좌우 N-1칸씩?

    #중앙줄부터 위로 합
    #중앙줄부터 아래 합
    #중앙줄 합 한번 빼기 _ 중복값
    #for i in range(N):
    
    #마름모에 해당하는 범위값 총합 출력





'''
내꺼만들기
https://www.acmicpc.net/workbook/view/20
'''
