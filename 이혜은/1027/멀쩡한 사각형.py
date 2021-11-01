def solution(w,h):

    tmp = 0
    
    if w <= h:
        until = w
    else:
        until = h
    for i in range(until, -1, -1):
        if h%i == 0 and w%i == 0:
            tmp = i
            break
            
    answer = w*h - (w+h-tmp)
    
    
    return answer