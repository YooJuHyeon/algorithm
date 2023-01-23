N, M = map(int,input().split())
A, B = [], []

for row in range(N):
    row = list(map(int,input().split()))
    A.append(row)

for row in range(N):
    row = list(map(int,input().split()))
    B.append(row)    

for row in range(N):
    for i in range(M):
        print(A[row][i] + B[row][i], end =' ')
    print()    