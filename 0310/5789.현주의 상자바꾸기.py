'''
0이 적힌 상자 N개를 동일한 숫자로 Q회 변경
L번부터 R번까지
인덱스와 값 숫자 차이 주의하기
arr 언패킹 프린트할 때 , 주의
'''


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1,T+1):
    N, Q = map(int, input().split()) #N 상자개수, Q 변경횟수
    arr = [0] * N  # 상자 초기상태 [00000]
    # print(arr)
    for i in range(1,Q+1) : #Q번 변경_ 숫자 바꾸는 횟수_Q회동안 일정 범위 상자를 동일한 숫자로 변경
        L, R = map(int, input().split()) #L번째부터 R번까지
        #L번부터 R번까지 범위 상자 숫자를 i로
        for j in range(L-1, R): #L번째부터 R번째까지_인덱스 숫자라서 -1(123 012) / R번째값은 미포함
            arr[j] = i #j번째 상자를 i값으로


    print(f'#{test_case}', *arr) #arr 언박싱
