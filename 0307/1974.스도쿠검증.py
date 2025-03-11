import sys
sys.stdin = open("input.txt", "r")


T = int(input()) #테스트케이스

for test_case in range(1,T+1):
    arr = [list(map(int,input().split())) for i in range(9)]
    print(arr)
    N = len(arr)
    print(N)

    #number = [1,2,3,4,5,6,7,8,9] #확인할 숫자 값 리스트

    # 이동하면서 확인
    # 가로 세로 1부터 9까지 숫자 한번씩
    for i in range(N):
        row_set = set()  # 가로확인
        col_set = set()  # 세로 확인
        # arr(i,j) 위치에서
        for j in range(N):
            row_set.add(arr[i][j])
            col_set.add(arr[i][j]) 

        if len(row_set) != N or len(col_set) != N:  # 길이가 N이 아니면
            answer = 0  # 잘 되어있지 않으면 0 출력

        # 3*3 작은 격자에서 1부터 9까지 숫자 한번씩

        ''' #작은 3*3배열의 왼쪽 위에서 시작해서 삼각형 범위 값이 잘 되어 있나 확인
        (0,0) (0,3), (0,6)
        (3,0), (3,3), (3,6)
        (6,0), (6,3), (6,6)
        '''  # 격자에서 (i,j)의 위치들
        for i in range(0, N, 3):
            for j in range(0, N, 3):
                box_set = set()
                # (r,c): 작은 정사각형 내에서 순회하는 위치
                for r in range(i, i + 3):
                    for c in range(j, j + 3):
                        box_set.add(arr[r][c])

                if len(box_set) != N:
                    answer = 0
        print(f'#{test_case} {answer}')

    # 겹치는 숫자가 없으면 1 출력
    # 아니면 0 출력


'''
내꺼만들기

set() : 집합자료형_중복제거, 무순서, 빠른 검색_존재여부확인, 중복체크, 포함여부 검사
name_set.add() : 해당 변수에 값 추가


배열 속 격자에서 값 확인하기
'''
