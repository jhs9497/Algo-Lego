def solution(s):
    n = len(s)
    min_count = n
    if n == 1:
        return 1
    for i in range(1, n // 2 + 1):
        now_pattern = s[:i]
        count = 1
        temp_word = ''
        for j in range(i, len(s), i):
            target_pattern = s[j:j + i]
            if now_pattern != target_pattern:
                if count > 1:
                    sum_pattern = str(count) + now_pattern
                    temp_word += sum_pattern
                else:
                    temp_word += now_pattern

                now_pattern = target_pattern
                count = 1

            else:
                count += 1

        if count > 1:

            sum_pattern = str(count) + now_pattern
            temp_word += sum_pattern

        else:
            temp_word += now_pattern

        if min_count > len(temp_word):
            min_count = len(temp_word)

    return min_count