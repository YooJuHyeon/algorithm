numbers = list(map(int,input().split()))
verification = 0

for i in numbers:
    verification += i**2
print(verification%10)
