N = int(input()) 
notcute, cute = 0, 0

for n in range(1, N+1):
    a = int(input())

    if a == 0:
        notcute+=1
    
    elif a == 1:
        cute+=1

if notcute > cute:
        print("Junhee is not cute!")
    
elif cute > notcute:
        print( "Junhee is cute!")   