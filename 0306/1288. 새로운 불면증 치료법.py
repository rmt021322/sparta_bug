T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input()) #시작값 N
    #다음값 2N 3N 4N
    count = 0 #곱할 상수값 초깃값 설정_반복문에서 개수 증가
    sleep_number = [ ] #세린 양 자릿수 숫자 넣을 리스트 
    #숫자 만나면 분해해서 리스트에 하나씩 집어넣기
    #0~9까지 범위 숫자 -> 리스트 길이는 10으로 하자
    
    #리스트에 0~9 숫자가 다 채워지는 순간 break
    #조건
    while len(sleep_number) < 10 : #길이가 10이 되면 종료
        count += 1 #반복문 돌때마다 1씩 증가
    #중복 숫자 만나면 덮어쓰거나 생략하거나
        sheep_number = N * count # 처음값 * count _ 현재 계산값
        #계산값의 숫자를 리스트에 저장
        for num in str(sheep_number): #계산값을 문자열로 변경
            if int(num) not in sleep_number : #문자열->정수 변경해서 낱개 숫자 꺼내고
                #그 숫자가 리스트 sleep_number에 없으면
                sleep_number += [int(num)] #리스트에 값 추가

    print(f'#{test_case} {sheep_number}') 
