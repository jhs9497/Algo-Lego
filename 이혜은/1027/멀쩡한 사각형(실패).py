def solution(w,h):
    answer = 0
    
    def line(x, y):
    # 대각선 공식을 구해보자
        if x == 0 and y == 0:
            return False
        
        if (h/w*x) - y == 0: # x = 2 y = 3 h&w = 3/2
            return True
        else:
            return False
    
    r = -1
    c = -1
    for i in range(w):
        for j in range(h):
            tmp = line(i, j)
            if tmp:
                r = i
                c = j
                break
        if r != -1:
            break
    
    if r == -1:
        return 0

    # (h/w*x) = y
    # x = y/h*w
    def include(x, y):
        
        if y <= (h/w*x) <= y+1:
            return True
        
        if y <= (h/w*(x+1)) <= y+1:  
            return True
        
        if (h/w*x) <= y <= (h/w*(x+1)):
            return True
        
        if (h/w*x) <= y+1 <= (h/w*(x+1)):
            return True
        
        return False
    
    tmp = 0 
    for i in range(r):
        meet = False
        for j in range(c):
            if include(i, j):
                meet = True
                tmp += 1
            
            elif meet:
                break
            
    
    answer = w*h - tmp*(w//r)
    
    
    return answer