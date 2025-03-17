# 0317 1220
import sys

sys.stdin = open("sample_input.txt", "r")

T = int(input())
N, M = map(int, input().split())  # 길이 n 횟수 m
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    for i in range(M):
        arr = [[0] * N for _ in range(N)]  # 바둑배열
        r, c, stone = map(int, input().split())  # (r,c) 위치에  stone놓기
        # 돌을 놓을 수 없는 곳은 주어지지 않는다
        for a in range(N):
            for b in range(N):
                arr[r][c] = stone  # arr(r,c) 위치에  stone놓기
    #
    print(f'#{test_case} {black} {white}')

'''
def change_color(arr, N, row, col, color)  #배열, 길이, 행, 열, 색):
    #가로, 세로, 대각선으로 놓을 돌과 놓인돌 사이
    #우하좌상 + 대각선 5시 7시 9시 1시
    dir = [(1,0), (0,-1), (-1,0), (0,1), (1,-1), (-1,-1), (-1,1), (1,1)]
    
    # 반대편 색상 저장하기
    if color == 1: #흑->백
        opposite = 2
    else : #백->흑
        opposite = 1
        
    for dr, dc in dir: #
        r, c = row+dr, col+dc
        position = [] #위치 저장할 리스트 생성
        
        #탐색
        while 0 <= r< N and 0<=c<N and arr[r][c] == opposite : #r,c가 범위 내면서 다른 색 돌이면
            position.append((r,c)) # 튜플(불변)로 position에 저장
            #위치이동
            r += dr
            c += dc
        
        #가능한 범위 내 색상 바꾸기
        if 0<=r<N and 0<=c<N and arr[r][c] == color : #범위 내에 내 색상 돌이 있으면
            #범위 안 다른 색 돌 찾아서
            arr[a][b] = color #그 돌 색을 내 색으로 바꾸기
        
        
        
###


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M =map(int, input().split()) #한 변 길이 N 돌 놓는 횟수 M
    for i in range(M): #
        row, column, color = map(int,input().split()) #돌 놓을 위치 row, column과 돌 색 color
        #돌을 놓을 수 없는 곳은 입력으로 주어지지 않음
        #흑돌 1 백돌 2
        
        
        #색 바꾸기
        change_color(arr, N, row, column, color)
        
        
        
    #게임 종료 후 흑돌, 백돌 수 출력하기
    blackstone = 0
    whitestone = 0
    
    for row in range(N):
        for col in range(N):
            if arr[row][col] == 1:
                blackstone+=1 #흑돌 개수 추가
            elif arr[row][col] == 2:
                whitestone += 1 #백돌 개수 증가
    return blackstone, whitestone
    #print(f'#{test_case} {blackstone} {whitestone}')
        
'''
