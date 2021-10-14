def solution(numbers, target):
    answer = 0
    def dfs(number, level):
        nonlocal answer
        if level == len(numbers):
            if number == target:
                answer += 1
            return

        dfs(number + numbers[level], level + 1)
        dfs(number - numbers[level], level + 1)

    dfs(0, 0)
    return answer