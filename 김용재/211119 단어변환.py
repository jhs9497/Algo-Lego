def solution(begin, target, words):
    answer = 0
    stack = []
    stack.append([begin,0])
    visited = len(words) * [0]
    if target not in words:
        answer = 0
    else:
        answer = bfs(target, words, stack, visited, 0)
    return answer


def bfs(target, words, stack, visited, depth):

    while stack:
        a = stack.pop(0)
        # print(a)
        begin = a[0]
        depth = a[1]
        if begin == target:
            return depth
        # print(begin,'ss')
        for i in range(len(words)):
            cnt = 0
            if visited[i] == 0:
                for j in range(len(words[i])):
                    if cnt > 1:
                        break
                    if begin[j] == words[i][j]:
                        continue
                    else:
                        cnt += 1
                if cnt == 1:
                    visited[i] = 1
                    stack.append([words[i],a[1]+1])
                    # print(stack)
                    # if words[i] == target:
                    #     return depth

begin ="hit"
target ="cog"
words =["hot", "dot", "dog", "lot", "log", "cog"]
print(solution(begin, target, words))