from collections import defaultdict

def solution(n, words):
    answer = []
    member_count = defaultdict(int)
    idx = 0
    words_list = []
    for i in range(len(words)):
        idx += 1
        if idx > n:
            idx = 1

        if i > 0:
            if words[i][0] != words[i - 1][-1]:
                answer.append(idx)
                member_count[idx] += 1
                answer.append(member_count[idx])
                break

        if words[i] in words_list:
            answer.append(idx)
            member_count[idx] += 1
            answer.append(member_count[idx])
            break
        else:
            member_count[idx] += 1
            words_list.append(words[i])

    if len(answer) == 0:
        answer = [0, 0]

    return answer