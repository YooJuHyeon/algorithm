def solution(price):
    
    if 500000 <= price <= 1000000:
        answer = int(price*0.8)
    elif 300000 <= price < 500000:
        answer = int(price*0.9)
    elif 100000 <= price < 300000:
        answer = int(price*0.95)
    else:
        answer = int(price)
    return answer