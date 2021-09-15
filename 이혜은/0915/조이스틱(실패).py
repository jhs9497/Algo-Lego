def solution(name):
    answer = 0
    
    count_A = 0
    for alpha in name:
        if alpha == 'A':
            count_A += 1
    if count_A == len(name):
        return 0
    
    right_check = [0 for _ in range(len(name))]
    left_check = [0 for _ in range(len(name))]
    
    for i in range(len(name)):
        if name[i] != 'A':
            right_check[i] = 1
    
    right = 0
    
    for i in range(len(name)):
        tmp = min(abs(ord(name[i])-ord('A')), abs(ord('A')+26-ord(name[i])))
        right_check[i] = 0
        answer += tmp + 1
        if sum(right_check) == 0:
            break
    answer -= 1
    
    right = answer
    
    answer = 0
    
    left = 0
    left_name = name[0]
    
    for i in range(len(name)-1, 0, -1):
        left_name += name[i]
        
    for i in range(len(left_name)):
        if left_name[i] != 'A':
            left_check[i] = 1

    for i in range(len(left_name)):
        tmp = min(abs(ord(left_name[i])-ord('A')), abs(ord('A')+26-ord(left_name[i])))
        left_check[i] = 0
        answer += tmp + 1
        if sum(left_check) == 0:
            break
        
    answer -= 1
    
    left = answer
    
    return answer