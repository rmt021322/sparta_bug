
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.

for test_case in range(1, T + 1):
    N, K = map(int, input().split()) #학생수 N, 학생 번호 K
    score_list = ["A+", "A0",  "A-", "B+", "B0", "B-", "C+", "C0", "C-", "D0"] #리스트에 평점 저장
    #print(score_list)
    total_list = [ ] #총점을 저장할 리스트
    for i in range(N):
        S, O, R = map(int, input().split())# 학생별 중간 기말 과제 점수_S중간 O기말 R과제
       #print(S)
        #중간 35 기말 45 과제 20 백분율
        personal_score = S*0.35+O*0.45+R*0.2
       # print(personal_score)
        total_list = total_list + [personal_score] #총점 리스트에 백분율값 추가
        
    
