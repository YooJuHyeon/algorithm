N = int(input())
rank_list = []    
rank = [1]*N                           # 랭킹 점수 리스트 모두 1로 셋팅

for i in range(N):
    kg, cm = map(int,input().split())
    rank_list.append([kg, cm])              # 입력받은 키와 몸무게를 이차원리스트 형태로 추가

for i in range(N):
    for j in range(N):              # 핼렬 순회

        # 이전 리스트[i행] 몸무게[0열]보다 다음리스트[j행]의 몸무게보다 크고, 
        # 이전리스트보다 다음 리스트의 키[1열]가 크다면
        if rank_list[i][0] < rank_list[j][0] and rank_list[i][1] < rank_list[j][1]:
            rank[i] += 1        # 랭크리스트 인덱스 i에 1 더하기

print(*rank)