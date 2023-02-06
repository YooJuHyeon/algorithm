count = 0
count_list = []

for i in range(1,5):
    off, on = map(int, input().split())
    a = count - off
    count = a + on
    count_list.append(count)

print(max(count_list))