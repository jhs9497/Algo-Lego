from collections import defaultdict

def solution(info, query):
    score_dict = defaultdict(list)
    answer = [0] * len(query)
    for i in range(len(info)):
        A, B, C, D, score = info[i].split()
        score = int(score)
        A_list = [A, '-']
        B_list = [B, '-']
        C_list = [C, '-']
        D_list = [D, '-']
        for q in range(2):
            for w in range(2):
                for e in range(2):
                    for r in range(2):
                        name = A_list[q] + B_list[w] + C_list[e] + D_list[r]
                        score_dict[name].append(score)

    for key in score_dict.keys():
        score_dict[key].sort()

    for i in range(len(query)):
        query_list = list(query[i].split())
        score = int(query_list.pop(-1))
        for _ in range(3):
            query_list.remove('and')

        Q = "".join(query_list)

        score_list = score_dict[Q]
        if len(score_list) > 0:
            left = 0
            right = len(score_list)
            while left < right:
                mid = (left + right) // 2
                if score_list[mid] >= score:
                    right = mid
                else:
                    left = mid + 1
            answer[i] = len(score_list) - left
        else:
            answer[i] = 0

    return answer