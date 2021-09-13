from itertools import permutations
from collections import deque
import math

def check_primary(number):
    if number <= 1:
        return False
    N = int(math.sqrt(number))
    print(number, N)

    for i in range(2, N + 1):
        if number % i == 0:
            return False

    return True

def solution(numbers):
    number_list = set()
    for i in range(1, len(numbers) + 1):
        case_list = deque(permutations(numbers, i))
        for j in range(len(case_list)):
            case = int(''.join(case_list[j]))
            number_list.add(case)

    number_list = deque(number_list)
    answer = 0
    for number in number_list:
        flag = check_primary(number)
        if flag == True:
            answer += 1

    return answer