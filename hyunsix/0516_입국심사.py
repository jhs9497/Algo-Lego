def solution(n, times):
    times.sort()
    left = 1
    right = n * times[-1]
    mid = 0

    answer = right

    while left <= right:
        mid = (left + right) // 2

        tmp_cnt = 0
        for i in range(len(times)):
            tmp_cnt += (mid // times[i])

        if tmp_cnt >= n:
            right = mid - 1
            answer = min(answer, mid)

        else:
            left = mid + 1

    return answer