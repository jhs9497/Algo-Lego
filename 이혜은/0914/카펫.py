import math

def solution(brown, yellow):
    
    answer = []
    
    b_lst = []
    y_lst = []
    
    brown += yellow
    
    for i in range(brown, int(math.sqrt(brown))-1, -1):
        if brown % i == 0:
            b_lst.append([i, brown//i])
    
    for i in range(yellow, int(math.sqrt(yellow))-1, -1):
        if yellow % i == 0 and i >= yellow//i:
            y_lst.append([i, yellow//i])

    for bx, by in b_lst:
        for yx, yy in y_lst:
            if bx - yx == 2 and by - yy == 2:
                return [bx, by]
    
    return answer