number_list = []
count_dict = {}

for i in range(10):
    number = int(input())
    number_list.append(number)
    
    if number in count_dict:
        count_dict[number] += 1
    else:
        count_dict[number] = 1

max = 0
for key, value in count_dict.items():
    if max < value:
        max = value
        mode = key

average = sum(number_list)/10
print(round(average), mode, sep='\n')