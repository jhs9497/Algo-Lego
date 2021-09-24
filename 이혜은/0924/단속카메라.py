def solution(routes):
    
    answer = 1
    
    routes = sorted(routes, key = lambda x : x[0])
    point = routes[len(routes)-1][0]
    
    for i in range(len(routes)-1, -1, -1):
        if point > routes[i][1]:
            answer += 1
            point = routes[i][0]
    
    return answer