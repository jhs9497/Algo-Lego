answer = 0
def solution(numbers, target):
    
    def make(num, now):
        
        global answer
        if now == len(numbers):
            if num == target:
                answer += 1
            return
        
        make(num+numbers[now], now+1)
        make(num-numbers[now], now+1)
    
    make(0, 0)
    
    return answer