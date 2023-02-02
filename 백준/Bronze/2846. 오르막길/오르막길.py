N = int(input())
numbers = list(map(int, input().split()))
temp = 0
uphill_road = []

for i in range(1, N):
    if numbers[i] > numbers[i-1]:
        temp += numbers[i] - numbers[i-1]
        if i == N-1:
            uphill_road.append(temp)
    
    else:
        uphill_road.append(temp)
        temp = 0

print(max(uphill_road))