matrix = [[0]*15 for _ in range(5)]

for i in range(5):
    word = input()
    
    for j in range(len(word)):
        matrix[i][j] = word[j]

for i in range(15):
    for j in range(5):
        if matrix[j][i] == 0:
            pass
        else:
            print(matrix[j][i], end='')
