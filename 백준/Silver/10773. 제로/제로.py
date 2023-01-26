account_book = []

K = int(input())

for i in range(1, K+1):
    money = int(input())

    if money ==0:
        account_book.pop()
    else:
        account_book.append(money)

print(sum(account_book))
