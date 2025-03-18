'''
    # stick 리스트 뒤집기_오른쪽에서 봤을 때 보이는 탑 개수
    # 리스트를 뒤집어서 왼쪽방향 탑이 오른쪽으로 오도록
    sorted(stick, reverse=True)?
    '''

N = int(input())
stick = [0] * N
count = 0  # 보이는 막대기 개수
highest = 0 #가장 높은 막대기 높이


for h in range(N): #stick 리스트에 높이 저장: N이 5일 때 인덱스 01234
    stick[h] = int(input())

    # print(stick)

for i in range(N-1, -1, -1): #리스트 뒤집기 :N-1부터 0번인덱스까지 역순으로
    if stick[i] > highest: #i번째 stick값이 최댓값보다 크면
        count += 1 #수량 증가하고
        highest = stick[i] #값도 저장

print(count)
