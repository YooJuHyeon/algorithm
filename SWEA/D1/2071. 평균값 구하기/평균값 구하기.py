T = int(input())
for t in range(1, T+1):
    numbers = list(map(int,input().split()))
    average = sum(numbers) / len(numbers)
    a = round(average)
    print(f"#{t} {a}")

