from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
my_deq = deque()

for i in range(N):
    command = input().split()

    if command[0] == "push_front":
        my_deq.appendleft(command[1])

    elif command[0] == "push_back":
        my_deq.append(command[1])

    elif command[0] == "pop_front":
        if len(my_deq) == 0:
            print("-1")
        else:
            print(my_deq[0])
            my_deq.popleft()

    elif command[0] == "pop_back":
        if len(my_deq) == 0:
            print("-1")
        else:
            print(my_deq[len(my_deq)-1])
            my_deq.pop()

    elif command[0] == "size":
        print(len(my_deq))

    elif command[0] == "empty":
        if len(my_deq) == 0:
            print("1")
        else:
            print("0")

    elif command[0] == "front":
        if len(my_deq) == 0:
            print("-1")
        else:
            print(my_deq[0])

    elif command[0] == "back":
        if len(my_deq) == 0:
            print("-1")
        else:
            print(my_deq[len(my_deq)-1])