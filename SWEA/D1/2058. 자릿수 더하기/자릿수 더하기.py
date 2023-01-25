number = int(input())
total = 0

while number > 0:
    n = number % 10
    total += n
    number = number // 10

print(total)    