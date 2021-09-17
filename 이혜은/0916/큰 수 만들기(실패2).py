def solution(number, k):
    remove_lst = []
    remove_k = 0
    answer = ''
    tmp = k
    
    for i in range(len(number)):
        for j in range(i+1, i+1+tmp):
            if j < len(number) and int(number[i]) < int(number[j]):
                remove_k += 1
                remove_lst.append(i)
                tmp -= 1
                break
        if remove_k == k:
            break    
    for i in range(len(number)):
        if i in remove_lst:
            continue
        answer += number[i]
    
    return answer