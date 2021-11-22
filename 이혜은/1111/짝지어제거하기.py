def solution(s):

    i = 0
    j = 1
    
    if len(s) == 0:
        return 1
    elif len(s) == 1:
        return 0
    
    lst = []
    
    for i in range(len(s)):
        if lst:
            tmp = lst[-1]
            if tmp == s[i]:
                lst.pop()
            else:
                lst.append(s[i])
        else:
            lst.append(s[i])
            
    if len(lst) == 0:
        return 1
    
    return 0