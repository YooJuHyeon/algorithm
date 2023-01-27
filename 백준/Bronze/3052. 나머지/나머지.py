remainder = []

for _ in range(10):
    numbers = int(input())
    remainder.append(numbers%42)

print(len(set(remainder)))
