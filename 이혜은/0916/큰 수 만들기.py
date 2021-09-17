def solution(number, k):
    answer = []
    
    for i in number:
        
        while answer and answer[-1] < i:
            if k > 0:
                answer.pop()
                k -= 1
            else:
                break
        
    if k > 0:
        for i in range(k):
            answer.pop()
            
    return ''.join(answer)