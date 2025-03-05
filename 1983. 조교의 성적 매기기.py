
T = int(input())
N, K = map(int, input().split()) #학생수 N, 학생 번호 K
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
score_list = ["A+", "A0",  "A-", "B+", "B0", "B-", "C+", "C0", "C-", "D0"] #평점리스트
total_list = [ ]
#print(score_list)
for test_case in range(1, T + 1):
    S, O, R = map(int, input().split())# 학생별 중간 기말 과제 점수_S중간 O기말 R과제
    #print(S)
    #중간 35 기말 45 과제 20 백분율
    personal_score = S*0.35+O*0.45+R*0.2
   # print(personal_score)
    total_list = total_list + [personal_score] #리스트에 값 추가
    print(total_list) #[74.6, 92.55000000000001]
    
