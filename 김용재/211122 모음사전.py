def solution(word):
    answer = 0
    check = ['A', 'E', 'I', 'O', 'U']
    sum_word = ''
    dfs(word, check, sum_word)
    return cnt

cnt = 0
flag = False

def dfs(word, check, sum_word):
    global flag
    global cnt

    if sum_word == word:
        answer = cnt
        flag = True
        print(sum_word, cnt)
        return answer

    if flag == True:
        return

    if len(sum_word) == 5:
        print(sum_word, cnt)
        return sum_word

    else:
        for c in check:
            if flag == True:
                return
            cnt += 1
            dfs(word, check, sum_word + c)



word = 'I'
print(solution(word))