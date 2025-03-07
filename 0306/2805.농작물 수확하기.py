T = int(input())
#print(arr)
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
N = int(input()) #농장 크기
for test_case in range(1, T + 1):
    arr = [list(map(int, input())) for j in range(N)] #농장의 농작물 가치
    
    #마름모 만들기
    #정중앙점 기준으로 행 N칸에서 시작해서
    middle = N//2
    start = (middle,middle) #시작점 중앙값


'''
0307 1632_돌뒤집기 하고 다시해보자
    #위아래 한층씩 갈수록 행 좌우 N-1칸씩

    #중앙줄부터 위로 합
    #중앙줄부터 아래 합
    #중앙줄 합 한번 빼기 _ 중복값
    #for i in range(N):
    
    #마름모에 해당하는 범위값 총합 출력
'''
    sum_crops = 0 #총합 초깃값
    for r in range(N): #가로 이동 횟수
        for c in range(N): #세로 이동 횟수
            if abs(r-middle) + abs(c-middle) <= middle: #가로값 세로값 절댓값 합이 middle보다 작으면
                #어디서 출발하든 목표지점은 가운데라 그 초과 미만으로는 갈 필요가 없다 배열 반절만 가자
                sum_crops += arr[r][c] #누적합

print(f'#{test_case} {sum_crops}') 

'''
내꺼만들기
https://www.acmicpc.net/workbook/view/20
좌표설정은 ☆(n,m)☆
강사님 풀이
농장배열 이차원배열 N*N 배열에서
기준잡는 정중앙 좌표값 middle이니까
-> 어느 지점에서 출발하든 도착할 중앙 지점 미만/초과 부분은 더 갈 필요가 없다
결국 도착지점은 배열 중앙에 있음

절댓값 abs() 파이썬 내장함수 이용



'''
