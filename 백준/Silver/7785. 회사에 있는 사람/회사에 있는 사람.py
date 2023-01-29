n = int(input())
enter = {}

for _ in range(n):
    a, b = input().split()
    
    if b == 'enter':
        enter[a] = b
    else:
        enter.pop(a)

enter = sorted(enter.keys(), reverse=True)

print(*enter, sep='\n')