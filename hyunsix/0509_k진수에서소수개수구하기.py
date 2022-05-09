import math

def solution(n, k):
    answer = 0 
    trans_n = ''
    while n > 0:
        remain = n % k
        trans_n = str(remain) + trans_n
        n = n // k
    
    prime_list = []
    
    number = ''
    for i in trans_n:
        if i != '0':
            number += i
        else:
            if number:
                prime_list.append(int(number))
                number = ''
    if number:
        prime_list.append(int(number))
    
    for i in prime_list:
        flag = True
        if i > 2:
            for j in range(2, int(math.sqrt(i))+1):
                if i % j == 0:
                    flag = False
                    break
        
        if i == 1:
            flag = False
            
        if flag:
            answer += 1
        
    return answer