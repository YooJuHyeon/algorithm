message = list(input())
happy = 0
sad = 0

for i in range(len(message)):
    if message[i] == '-':
        if message[i+1] == ')':
            happy += 1
        elif message[i+1] == '(':
            sad+= 1

if happy == sad != 0:
    print('unsure')
elif happy > sad:
    print('happy')
elif happy < sad:
    print('sad')
elif happy == sad == 0:
    print('none')
