import sys

T = int(sys.stdin.readline()) 

for t in range(1, T+1):
    A, B = map(int, sys.stdin.readline().split())
    print(A+B)

