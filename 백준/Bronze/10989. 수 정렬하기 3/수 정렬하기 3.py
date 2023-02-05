import sys

N = int(sys.stdin.readline())
arr = [0]*10000         # 10,000개의 수를 담을 수 있는 배열 만들기
                        # (문제조건 中 "입력에는 10,000개보다 작거나 같은 자연수가 주어진다.")
for _ in range(N):
    number = int(sys.stdin.readline())
    arr[number-1] += 1  # 입력받은 수에 해당하는 인덱스에 1더하기

for i in range(10000):   # 배열 크기만큼 순회
    if arr[i] != 0:      # 값이 0이 아니라면
        for j in range(arr[i]): # 인덱스에 해당하는 숫자를 출력
            print(i+1)