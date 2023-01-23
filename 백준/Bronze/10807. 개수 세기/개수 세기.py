N = int(input())
numbers = list(map(int,input().split()))
V = int(input())
cnt = 0


for t in numbers:
    if t == V:
        cnt += 1
print(cnt)        