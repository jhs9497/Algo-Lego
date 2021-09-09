def check(p):
    is_open = 0
    u = ""
    v = ""
    for i in range(len(p)):
        if p[i] == '(':
            is_open += 1
        else:
            is_open -= 1

        if i > 0 and is_open == 0:
            u = p[0:i + 1]
            v = p[i + 1:]
            break

    is_open = 0
    for i in range(len(u)):
        if u[i] == '(':
            is_open += 1
        else:
            if is_open > 0:
                is_open -= 1

    if is_open == 0:
        return u, v, True

    return u, v, False


def solution(p):
    if len(p) == 0:
        return ""

    is_open = 0
    for i in range(len(p)):
        if p[i] == '(':
            is_open += 1
        else:
            if is_open > 0:
                is_open -= 1
    if is_open == 0:
        return p

    u, v, correct = check(p)
    answer = ""
    
    if correct:
        return u + solution(v)

    else:
        answer = '(' + solution(v) + ')'
        for i in range(1, len(u) - 1):
            if u[i] == '(':
                answer += ')'
            else:
                answer += '('

    return answer