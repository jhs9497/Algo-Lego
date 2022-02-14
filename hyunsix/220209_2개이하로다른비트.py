def trans_binary(n):
    N = int(n)
    binaryN = ''
    while N > 0:
        binaryN = str(N % 2) + binaryN
        N = N // 2

    if n % 2 == 1:
        binaryN = '0' + binaryN

    return binaryN


def check_min(binaryN):
    binaryN = list(binaryN)
    if binaryN[-1] == '0':
        binaryN[-1] = '1'
        return binaryN
    for i in range(len(binaryN) - 1, -1, -1):
        if binaryN[i] == '0':
            binaryN[i] = '1'
            binaryN[i + 1] = '0'
            return binaryN

    return binaryN


def trans_demical(min_N):
    min_N.reverse()
    ans = 0
    for i in range(len(min_N)):
        if min_N[i] == '1':
            ans += (2 ** i)
    return ans


def solution(numbers):
    answer = []
    for n in numbers:
        if n != 0:
            binaryN = trans_binary(n)
            min_N = check_min(binaryN)
            ans_N = trans_demical(min_N)
            answer.append(ans_N)
        else:
            answer.append(1)
    return answer