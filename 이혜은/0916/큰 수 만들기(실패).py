import itertools

def solution(number, k):
    answer = -1
    num_lst = []
    
    for num in number:
        num_lst.append(int(num))
    
    k = len(number) - k
    
    numbers = list(itertools.combinations(num_lst, k))
    
    for number in numbers:
        number = int("".join(map(str, number)))
        answer = max(answer, number)
    
    return str(answer)