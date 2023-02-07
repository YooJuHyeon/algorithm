N = int(input())
members = []

for i in range(N):
    A, B = input().split()

    members.append([int(A), i, B])

sorted_members = sorted(members)

for j in range(N):
    print(sorted_members[j][0], sorted_members[j][2])