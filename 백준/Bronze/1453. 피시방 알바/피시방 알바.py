N = int(input())
customer_want = list(map(int,input().split()))
reject = 0
seat = []

for i in range(N):
    if customer_want[i] in seat:
        reject += 1
    elif customer_want[i] not in seat:
        seat.append(customer_want[i])
        
print(reject)