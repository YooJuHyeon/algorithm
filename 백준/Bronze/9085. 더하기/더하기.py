T = int(input())  # 테스트케이스의 개수

for t in range(T):
    N = int(input())  # 자연수의 개수

    numbers = list(map(int,input().split())) # 공백이 있는 자연수들
    print(sum(numbers)) # 자연수의 합
