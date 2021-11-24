answer = 0
def solution(numbers, target):
    global answer
    dfs(numbers, target, 0)
    return answer

def dfs(numbers, target, depth):
    global answer

    if depth == len(numbers):
        if sum(numbers) == target:
            answer += 1
            return
        else:
            return
    else:
        dfs(numbers, target, depth+1)
        numbers[depth] *= -1
        dfs(numbers, target, depth+1)
        return


numbers = [1,1,1,1,1]
target = 3
solution(numbers, target)