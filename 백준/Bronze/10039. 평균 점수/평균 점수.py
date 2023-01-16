numbers = []

for n in range(5):
    score = int(input())
    
    if score < 40:
        score = 40
    
    numbers.append(score)

print(int(sum(numbers)/5))