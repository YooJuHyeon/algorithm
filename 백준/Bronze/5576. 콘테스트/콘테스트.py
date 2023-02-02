W_score = []
K_score = []

for _ in range(10):
    W = int(input())
    W_score.append(W)

for _ in range(10):
    K = int(input())
    K_score.append(K)

W_max = sum(sorted(W_score)[7:])
K_max = sum(sorted(K_score)[7:])

print(W_max, K_max)