#총점 내림차순에서 k의 점수 찾기 :k점수 == 총점
#백분율 10% 비율마다 같은 평점

T = int(input())  # 테스트 케이스 개수
for test_case in range(1, T + 1):
    N, K = map(int, input().split()) #학생수 N, 학생 번호 K
    score_list = ["A+", "A0",  "A-", "B+", "B0", "B-", "C+", "C0", "C-", "D0"] #리스트에 평점 저장
    total_list = [ ] #리스트에 총점 저장

    for i in range(N): #전체학생수 N
        S, O, R = map(int, input().split())# 학생별 중간 기말 과제 점수_S중간 O기말 R과제
        #print(S)
        #중간 35 기말 45 과제 20 백분율
        personal_score = S*0.35+O*0.45+R*0.2
        # print(personal_score)
        total_list.append(personal_score)  # 리스트에 값 추가
        #print(total_list) 
        
        #k번째 학생 점수 찾기
        k_score = total_list[K - 1]  # K번 학생의 총점
        #print(k_score) #하나 나와야 함
        
        
    # 성적을 내림차순으로 정렬
    #성적-평점 잇기
    #1. 총점리스트 줄세우기
    #버블정렬 내림차순
    for i in range(N - 1):
        for j in range(N - 1 - i):
            if total_list[j] < total_list[j + 1]:  # 앞의 값이 작으면
                total_list[j], total_list[j + 1] = total_list[j + 1], total_list[j]  # 위치 교환
            #print(total_list)  
   
    #k번째가 정렬후 리스트에서 몇번째인지 찾기
    rank = total_list.index(k_score)
    #print(rank) 
    
    #10%단위 
    rank_division = N // 10  # 10% 단위로 나누기

    #상위 10%부터 A+ A0 A- .... D0 부여하기
    final_rank = score_list[rank // rank_division]  # 등급 계산

    print(f'#{test_case} {final_rank}')
    '''
    #내꺼만들기#
    
    total_list.append(personal_score)  # 창작 리스트에 저장 값 추가할때 사용
    : total_list = total_list + [personal_score] 축약코드
    
     #k번째가 정렬후 리스트에서 몇번째인지 찾기
    rank = total_list.index(k_score)
    #print(rank) 
    
    #10%단위 
    rank_division = N // 10  # 10% 단위로 나누기

    #상위 10%부터 A+ A0 A- .... D0 부여하기
    final_rank = score_list[rank // rank_division]  # 등급 계산

    print(f'#{test_case} {final_rank}')
    '''
