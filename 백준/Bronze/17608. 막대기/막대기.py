import sys
input = sys.stdin.readline 

N = int(input())
stack = []
cnt = 1

for _ in range(N):
    number = int(input())
    stack.append(number)

last = stack.pop()
for i in range(N-1):
    high = stack.pop()

    if high > last:
        cnt +=1
        last = high
        
print(cnt)