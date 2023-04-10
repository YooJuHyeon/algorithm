def solution(array):
    answer = []
    
    a = max(array)
    b = array.index(a)
    
    answer.append(a)
    answer.append(b)
    
    return answer