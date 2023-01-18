T = int(input()) 

for t in range(1, T+1):
    sentence = list(input().split()) 
    for s in sentence:
        print(s[::-1], end=" ")