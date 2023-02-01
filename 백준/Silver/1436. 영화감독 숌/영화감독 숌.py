N = int(input())
number = 666                  # 제일 작은 종말의 숫자 설정
count = 0                     

while True:
    if '666' in str(number):    # while 루프안에서 number에 666 있으면 1씩 카운트하기
        count +=1
    if count == N:              # 카운트해준것과 N번째가 같을때는, number 출력하고 반복문 멈추기
        print(number)
        break
    number += 1     