N = int(input())
cup = [0, 1, 2, 3]

for _ in range(N):
    X, Y = map(int, input().split())
    cup[X], cup[Y] = cup[Y], cup[X]

print(cup.index(1))