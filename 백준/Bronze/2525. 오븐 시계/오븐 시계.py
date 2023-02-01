A, B = list(map(int, input().split()))
C = int(input())

if B + C > 59:
    A += (B+C)//60
    B = (B+C)%60
    if A > 23:
        A = A-24
else:
    B = B+C

print(A, B)    