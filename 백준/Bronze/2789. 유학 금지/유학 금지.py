word = input()
alphabet = 'CAMBRIDGE'

for i in word:
    if i in alphabet:
        word = word.replace(i, '')

print(word)    
