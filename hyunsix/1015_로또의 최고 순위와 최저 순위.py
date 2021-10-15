def solution(lottos, win_nums):
    zero_count = lottos.count(0)
    same_count = 0
    for number in lottos:
        if number in win_nums:
            same_count += 1

    max_count = zero_count + same_count
    min_count = same_count

    high_rank = 0
    if max_count == 0:
        high_rank = 6
    else:
        high_rank = 7 - max_count

    low_rank = 0
    if min_count == 0:
        low_rank = 6
    else:
        low_rank = 7 - min_count
    answer = [high_rank, low_rank]
    return answer