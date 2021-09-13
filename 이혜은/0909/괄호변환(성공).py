def solution(p):
    
    if len(p) == 0:
        return ""
    
    perfect = True
    tmp = 0
    for i in p:
        if i =='(':
            tmp += 1
        else:
            tmp -= 1
        
        if tmp < 0:
            perfect = False
            break
    
    if perfect == True:
        return p
    
    tmp = 0
    u = ''
    tmp_i = 0
    for i in range(len(p)):
        tmp_i = i
        if p[i] =='(':
            tmp += 1
            u += '('
        else:
            tmp -= 1
            u += ')'
        if tmp == 0:
            break
    
    if tmp_i+1 == len(p):
        v = ""
    else:
        v = p[tmp_i+1:]
    
    stop = False
    tmp = 0
    for i in u:
        if i =='(':
            tmp += 1
        else:
            tmp -= 1
        
        if tmp < 0:
            stop = True
            break
    
    if stop == False:
        return u + solution(v)
    else:
        tmp_u = ''
        for i in range(1, len(u)-1):
            if u[i] == '(':
                tmp_u += ')'
            else:
                tmp_u += '('
        return '(' + solution(v) + ')' + tmp_u