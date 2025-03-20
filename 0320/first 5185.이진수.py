#16진수->2진수 변환
#2진수 앞자리 0 반드시 출력

T = int(input()) #테스트케이스 수
for testcase in range(1,T+1):
    N, nhex = input(). split()
    savebin = ""

    hexmap = "0123456789ABCDEF"
    
    #16to10 : 각 자리 * 거듭제곱
    saveint = 0
    for i in range(len(nhex)):
        #뒤에서부터 한자리씩 가져와서 거듭제곱
        #16진수 = 마지막 자릿수가 16**0
        #1A3F = 1*(16**3) + A*(16**2) + 3*(16**1) + F*(16**0)
        saveint += hexmap.index(nhex[-(i+1)]) * (16**i)
    #print(saveint)

    #10to2 : 2로 나눠 나머지저장
    if saveint == 0:
        savebin = "0"
    else :
        while saveint >0:
            savebin = str(savebin%2) + savebin #0101 이진수 만들기
            saveint //= 2 #몫 업데이트

    #앞자리 0 보장하기
    lenbin= 4 * int(N)  #16진수 1자리 = 2진수 4자리
    while len(savebin) < lenbin :
       savebin = "0" + savebin 


    print(f'#{testcase} {savebin}')










