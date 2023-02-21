import sys
input = sys.stdin.readline

N = int(input())
my_dict = {}                     # 빈 딕셔너리 생성

for i in range(N):                    # 파일 개수만큼 반복문 돌리기
    file = input().rstrip().split('.')[1]      # file = .으로 구분해서 입력받은 리스트의 두번째 값(index=1)
    
    if file in my_dict:               # 만약 my_dict에 file이 있다면 1 더하기
        my_dict[file] += 1
    else:                             # 만약 my_dict에 file이 없다면
        my_dict[file] = 1             # my_dict의  key = file, value = 1로 설정


for key, value in sorted(my_dict.items()):   # 딕셔너리의 키-값 쌍으로 순회(with 키를 오름차순정렬해서)
    print(key, value)     