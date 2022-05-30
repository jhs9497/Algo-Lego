def solution(n):
    if n <= 2:
        return n
    
    answer = 0
    a = 1
    b = 2
    for _ in range(2, n):
        a, b = b, a+b
        
    answer = b % 1234567
    
    return answer