def change_color :
    #가로, 세로, 대각선으로 놓을 돌과 놓인돌 사이
    #우하좌상 + 대각선 5시 7시 9시 1시
dir = [(1,0), (0,-1), (-1,0), (0,1), (1,-1), (-1,-1), (-1,1), (1,1)]
    
    # 다른 색 돌을 내 색으로 바꾸기
    if color == 1: #흑->백
        color = 2
    else : #백->흑
        color = 1
        
###


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M =map(int, input().split()) #한 변 길이 N 돌 놓는 횟수 M
    for i in range(M): #
        row, column, color = map(int,input().split()) #돌 놓을 위치 row, column과 돌 색 color
        #돌을 놓을 수 없는 곳은 입력으로 주어지지 않음
        #흑돌 1 백돌 2
        
        
        
    #게임 종료 후 흑돌, 백돌 수 출력하기
    #print(f'#{test_case} {blackstone} {whitestone}')
        

