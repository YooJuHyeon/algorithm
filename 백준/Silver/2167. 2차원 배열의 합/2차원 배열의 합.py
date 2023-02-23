import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = []

for _ in range(N):
    number = list(map(int, input().split()))
    arr.append(number)                       

K = int(input())
sum = 0

for _ in range(K):
    i, j, x, y = list(map(int, input().split()))

# 행 i부터 행 x+1(인덱스떄문에 +1)까지 반복문, 열 j부터 열 y까지 반복문 돌려서 순회하면서, 더하기
    for a in range(i, x+1):
        for b in range(j, y+1):
            sum += arr[a-1][b-1]
    print(sum)
    sum = 0
