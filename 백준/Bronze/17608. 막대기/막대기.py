import sys
input = sys.stdin.readline 

N = int(input())
stack = []
cnt = 1                      # 마지막 막대기의 값은 1로 카운트 해놓기

for _ in range(N):
    number = int(input())
    stack.append(number)

high = stack.pop()
for i in range(N-1):
    last = stack.pop()

    if last > high:
        cnt +=1
        high = last
        
print(cnt)
