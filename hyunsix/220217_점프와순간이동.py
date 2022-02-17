def solution(n):
    # 일단 1칸 앞으로 전진
    ans = 1

    while n > 2:
        if n % 2:
            ans += 1
        n = n // 2

    return ans