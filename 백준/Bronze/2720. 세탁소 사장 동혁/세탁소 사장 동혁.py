T = int(input())

Quarter = 25
Dime = 10
Nickel = 5
Penny = 1

for i in range(T):
    C = int(input())
    
    print(C//Quarter, (C%Quarter)//Dime, (C%Quarter%Dime)//Nickel, (C%Quarter%Dime%Nickel)//Penny)      