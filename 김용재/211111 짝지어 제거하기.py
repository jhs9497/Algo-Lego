# from collections import deque
def solution(s):
    answer = -1
    # s = deque(s)
    s = list(s)
    print(s)
    def check(s):
        if len(s) == 0:
            return
        else:
            for i in range(len(s)-1):
                if s[i] == s[i+1]:
                    s.pop(i)
                    s.pop(i)
                    break
                else:
                    continue
        return check(s)
    check(s)
    if len(s) == 0:
        answer = 1
    else:
        answer = -1

    return answer
s = 'baabaa'
solution(s)