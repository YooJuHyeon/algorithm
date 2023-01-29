word = list(input())
old_phone = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
time = 0

for i in range(len(word)):
    for j in old_phone:
        if word[i] in j:
            time += old_phone.index(j)+3

print(time)