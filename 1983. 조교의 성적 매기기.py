T = int(input())  # 테스트 케이스 개수
for test_case in range(1, T + 1):
    N, K = map(int, input().split()) #학생수 N, 학생 번호 K
    score_list = ["A+", "A0",  "A-", "B+", "B0", "B-", "C+", "C0", "C-", "D0"] #리스트에 평점 저장
    total_list = [ ] #리스트에 총점 저장

    for i in range(N):
        S, O, R = map(int, input().split())# 학생별 중간 기말 과제 점수_S중간 O기말 R과제
        #print(S)
        #중간 35 기말 45 과제 20 백분율
        personal_score = S*0.35+O*0.45+R*0.2
        # print(personal_score)
        total_list = total_list + [personal_score] #리스트에 값 추가
        #print(total_list)

    # 성적을 내림차순으로 정렬하고, K번 학생의 성적 순위를 찾기
    #성적-평점 잇기
    #1. 총점리스트 줄세우기
    #버블정렬 내림차순
    for i in range(N - 1):
        for j in range(N - 1 - i):
            if total_list[j] < total_list[j + 1]:  # 앞의 값이 작으면
                total_list[j], total_list[j + 1] = total_list[j + 1], total_list[j] #위치 교환
            #print(total_list)  
    k_score = total_list[K - 1]  # K번 학생의 총점
    rank =total_list.index(k_score)  # k번째 학생 랭크 찾기
    #print(rank)


    #K값의 점수가 상위 10%이면 A+주고 90%면 D0 평점 부여하는 조건 만들기
for rank in range(1, N+1):
    #점수 기준 : rank값 순위
    final_rank = 0
    #rank/10해서 0.n이면 A+
        if rank/10 < 1 : #오류
            final_rank = score_list[0]
        #1.n이면 a0
        elif 1<=rank/10 < 2:
            final_rank = score_list[1]
         #2.n이면 a-
        elif 2<=rank/10 < 3:
            final_rank = score_list[2]
         #3.n이면 a0
        elif 3<=rank/10 < 4:
            final_rank = score_list[3]
         #4.n이면 a0
        elif 4<=rank/10 < 5:
            final_rank = score_list[4]
         #5.n이면 a0
        elif 5<=rank/10 < 6:
            final_rank = score_list[5]
         #6.n이면 a0
        elif 6<=rank/10 < 7:
            final_rank = score_list[6]
         #7.n이면 a0
        elif 7<=rank/10 < 8:
            final_rank = score_list[7]
         #8.n이면 a0
        elif 8<=rank/10 < 9:
            final_rank = score_list[8]
        #9.n이면 a0
        elif 9<=rank/10 :
            final_rank = score_list[9]
        else :
            break


print(f'#{test_case} {final_rank}')
    

