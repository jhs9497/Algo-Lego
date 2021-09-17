def solution(people, limit):
    answer = 0
    
    i = 0
    j = len(people)-1
    
    people = sorted(people)
    
    while i <= j:
        if people[i] + people[j] <= limit:
            i += 1
            j -= 1
        else:
            j -= 1
        answer += 1
    
    return answer