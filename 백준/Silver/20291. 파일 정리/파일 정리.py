N = int(input())
my_dict = {}

for i in range(N):
    file = input().split('.')[1]
    
    if file in my_dict:
        my_dict[file] += 1
    else:
        my_dict[file] = 1


for key, value in sorted(my_dict.items()):
    print(key, value)
