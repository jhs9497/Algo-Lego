def solution(k, dungeons):
    
    answer = 0
    
    visited = [False]*len(dungeons)
    
    def adventure(s, health):
        
        nonlocal answer 
        
        if s == len(dungeons):
            answer = s
            return
        
        if s > answer:
            answer = s
            
        for i in range(len(dungeons)):
            if not visited[i] and dungeons[i][0] <= (k-health):
                visited[i] = True
                adventure(s+1, health+dungeons[i][1])
                visited[i] = False
    
    adventure(0, 0)
    
    return answer