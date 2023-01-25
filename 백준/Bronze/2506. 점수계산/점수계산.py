N = int(input())
numbers = list(map(int,input().split()))
score = 0
sum_score = 0

for i in range(N):
    if numbers[i] == 1:
        score += 1
        sum_score += score
    elif numbers[i] == 0:
        score = 0

print(sum_score)        
