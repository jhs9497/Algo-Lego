def solution(cacheSize, cities):
    answer = 0
    cache = []
    for city in cities:
        city = city.lower()
        if city not in cache:
            if len(cache) < cacheSize:
                cache.append(city)
            else:
                if cacheSize > 0:
                    cache.pop(0)
                    cache.append(city)
            answer += 5

        else:
            cache.pop(cache.index(city))
            cache.append(city)
            answer += 1

    return answer