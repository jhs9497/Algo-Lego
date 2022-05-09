def solution(arr):
    answer = 0
    M = max(arr)
    L = len(arr)
    
    while True:
        i = M
        cnt = 0
        for j in arr:
            if i % j != 0:
                break
            else:
                cnt += 1
        if cnt == L:
            answer = i
            break
            
        M += 1
            
    return answer