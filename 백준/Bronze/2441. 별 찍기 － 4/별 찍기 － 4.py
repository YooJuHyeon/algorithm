N = int(input())

for i in range(1, N+1):
    a = ' ' * (i-1)
    b = '*' * (N+1-i)
    print(a+b)