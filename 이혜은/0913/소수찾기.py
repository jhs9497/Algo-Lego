import itertools
import math

def solution(numbers):
    answer = 0
    
    raw_num_lst = list(numbers)
    num_lst = [] 
    
    for i in range(1, len(numbers)+1):
        nums = list(itertools.permutations(raw_num_lst, i))
        for num in nums:
            tmp = int("".join(num))
            num_lst.append(tmp)
    
    check_lst = [False]*(max(num_lst)+1)
    
    def is_prime_number(num):
    
        if num == 0 or num == 1 or check_lst[num]:
            return False
        
        check_lst[num] = True

        for i in range(2, num//2+1):
            if num % i:
                continue
            return False
        
        return True
    
    def is_prime_number_2(num):
        
        if num == 0 or num == 1 or check_lst[num]:
            return False
        
        check_lst[num] = True

        for i in range(2, int(math.sqrt(num))+1):
            if num % i:
                continue
            return False
        
        return True
    
    for num in num_lst:
        if is_prime_number_2(num):
            answer += 1
    
    return answer