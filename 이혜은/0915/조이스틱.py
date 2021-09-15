def solution(name):
    answer = 0
    
    count_A = 0
    for alpha in name:
        if alpha == 'A':
            count_A += 1
    if count_A == len(name):
        return 0
    
    check = [0 for _ in range(len(name))]
    
    zero_lst = []
    ans_lst = []
    
    for i in range(len(name)):
        check[i] = min(abs(ord(name[i])-ord('A')), abs(ord('A')+26-ord(name[i])))
        if check[i] == 0:
            zero_lst.append(i)

    tmp = 0
    tmp_lst = check[::]
    
    for i in range(len(tmp_lst)):
        tmp += tmp_lst[i] + 1
        tmp_lst[i] = 0
        if sum(tmp_lst) == 0:
            break
            
    tmp -= 1
    
    ans_lst.append(tmp)
    
    tmp_lst = []
    tmp_lst.append(check[0])
    
    for i in range(len(check)-1, 0, -1):
        tmp_lst.append(check[i])
    
    tmp = 0
    for i in range(len(tmp_lst)):
        tmp += tmp_lst[i] + 1
        tmp_lst[i] = 0
        if sum(tmp_lst) == 0:
            break
        
    tmp -= 1
    
    ans_lst.append(tmp)
    
    for zero_point in zero_lst:
        
        left = zero_point
        right = zero_point
        
        while left >= 0:
            
            if name[left] == 'A':
                left -= 1
            else:
                break
                
        while right < len(check):
            if name[right] == 'A':
                right += 1
            else:
                break
                
        if left == -1 or right == len(check):
            continue
        else:
            # tmp = min(sum(check[:left+1])+sum(check[right:])+left*2+len(name)-right
            #           , sum(check[:left+1])+sum(check[right:])+left+(len(name)-right)*2)
            # 문제 내 맘대로 풀지 말기....
            tmp = sum(check[:left+1])+sum(check[right:])+left*2+len(name)-right
            
            ans_lst.append(tmp)
            
    answer = min(ans_lst)
    
    return answer