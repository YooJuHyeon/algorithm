start = input()
question = 0

while True:
    word = input()
    
    if word == '고무오리 디버깅 끝':
        break
    else:
        if word == '고무오리':
            if question == 0:
                question += 2
            else:
                question -= 1
        if word == '문제':
            question += 1

if question == 0:
    print('고무오리야 사랑해')
else:
    print('힝구')