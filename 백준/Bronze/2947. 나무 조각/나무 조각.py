numbers = list(map(int, input().split()))

while True:

    for n in range(4):
        if numbers[n] > numbers[n+1]:
            numbers[n], numbers[n+1] = numbers[n+1], numbers[n]
            print(*numbers) 

    if numbers == [1, 2, 3, 4, 5]:
        break
