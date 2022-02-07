def solution(cacheSize, cities):
    
    answer = 0
    
    cache = []
    cache_hit = 0
    time = 0
    
    if cacheSize == 0:
        return 5 * len(cities)
    
    for i in range(len(cities)):
        
        flag = False
        
        for j in range(len(cache)):
            if cache[j].upper() == cities[i].upper():
                cache.pop(j)
                cache.append(cities[i])
                flag = True
                time += 1
                break
                
        if flag:
            continue
        
        if len(cache) < cacheSize:
            cache.append(cities[i])
            
        else:
            cache.pop(0)
            cache.append(cities[i])
            
        time += 5
        
        
    return time