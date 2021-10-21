def solution(maps):
    answer = 100000
    i = 0
    j = 0

    N = len(maps[0])
    M = len(maps)

    cnt = 0
    # 상 하 좌 우
    di = [0, 0, -1, 1]
    dj = [-1, 1, 0, 0]

    # 도착할때까지
    while i == N - 1 and j == M - 1:
        for d in range(4):
            new_i = i + di[d]
            new_j = j + dj[d]

            # 인덱스 안에 들고 1일때
            while 0 <= new_i < N and 0 <= new_j < M and map[new_i][new_j] == 1:
                cnt += 1
                new_i += di[d]
                new_j += dj[d]
    print(cnt)

    return answer
maps = input()
solution(maps)