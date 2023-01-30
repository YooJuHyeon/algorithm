score = []

for _ in range(5):
    numbers = list(map(int, input().split()))
    score.append(sum(numbers))

print(score.index(max(score))+1, max(score))    