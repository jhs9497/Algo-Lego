from itertools import permutations


def check_count(case, k):
    now_fatigue = k
    count = 0
    for c in case:
        min_fatigue = c[0]
        if now_fatigue >= min_fatigue:
            count += 1
            now_fatigue -= c[1]
        else:
            return count
    return count


def solution(k, dungeons):
    N = len(dungeons)
    answer = -1
    cases = list(permutations(dungeons, N))
    for case in cases:
        count = check_count(case, k)
        if answer < count:
            answer = count

    return answer