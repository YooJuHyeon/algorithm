matrix = [[0]*100 for _ in range(100)]           # 100 X 100 행렬 만들기(리스트 컴프리헨션으로 작성)
area = 0                                         # 면적 = 0

for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())   # 네 정수 입력받기

    for i in range(x1, x2):                      # x1~X2 까지 반복문 돌리기
        for j in range(y1, y2):                  # 그 안에서 y1~y2 반복문 돌리기
           
           if matrix[i][j] == 0:                 # 행렬의 xi,yj 좌표가 0이라면(아직 1로 채워지지 않았다면)
            matrix[i][j] += 1                    # 해당 좌표에 1 더하고
            area +=1                             # 면적에 1 더하기

print(area)                                      # 면적 출력