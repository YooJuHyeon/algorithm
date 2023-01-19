result = []                  # 결과값 리스트(빈통)

for n in range(7):           # 7개의 자연수 받기
    numbers = int(input())   

    if numbers % 2 ==1:      # 홀수면 그 숫자를 결과값 리스트에 추가하기
        result.append(numbers)

if len(result)==0:            # 홀수가 존재하지 않는 경우(결과값 비어있음) -1 출력
            print(-1)

else:
    print(sum(result))           # 결과값 리스트의 합 출력
    print(min(result))           # 결과값 리스트 중 최소값