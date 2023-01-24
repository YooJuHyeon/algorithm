T = int(input())

for t in range(1, T+1):
    OX = input()
    score = 0
    sum_score = 0
    
    for i in OX:
        if i == 'O':
            score += 1
        else:
            score = 0

        sum_score += score
    print(sum_score)