N = int(input())

if N % 5 == 0:
    print(N//5)

else:
    cnt = 0

    while N > 0:
        N -= 3
        cnt +=1

        if N % 5 == 0:
            cnt += N // 5
            print(cnt)
            break

        else:
            if N == 0:
                print(cnt)
                break

            elif 0< N < 3:
                print('-1')
                break