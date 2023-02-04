word = input().upper()          # 대문자로 입력받기
word_list = list(set(word))     # 중복 제거헤서 리스트에 저장
my_dict = {}                    # 빈 딕셔너리 만들기
mode = []

for i in word_list:             # 중복 제거한 알파벳리스트 순회
    my_dict[i] = word.count(i)  # 딕셔너리에 삽입 (키=i, value=word에서 i 카운트한 값)

max_count = max(my_dict.values())

for key, value in my_dict.items(): 
    if max_count == value:
        mode.append(key)

if len(mode) > 1:
    print('?')
else:
    print(*mode)