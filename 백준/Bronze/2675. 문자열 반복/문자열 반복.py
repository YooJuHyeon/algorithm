T = int(input()) 

for t in range(1, T+1):
    R, S = input().split()
    P = ''

    for i in S :
        P += i*int(R)

    print(P)    
