from collections import deque

def solution(priorities, location):
    answer = 0
    
    N = len(priorities)
    
    lst = deque()
    for i in priorities:
        lst.append(i)
    
    seq = deque()
    for i in range(N):
        if location == i:
            seq.append(1)
        else:
            seq.append(0)

    while lst:
        tmp = lst.popleft()
        now = seq.popleft()
        
        if len(lst) == 0:
            answer += 1
            break
            
        max_tmp = max(lst)
        
        if tmp >= max_tmp:
            answer += 1
            if now == 1:
                break
                
        else:
            lst.append(tmp)
            seq.append(now)
            
    
    return answer