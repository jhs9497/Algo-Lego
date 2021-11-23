def solution(seat):
    print(seat)
    answer = 0
    L = len(seat)
    visited = [[0] * L for _ in range(L)]
    # print(visited)
    # 1,2,3번째줄 순서
    di = [-1,-1,-1, 0,0, 1,1,1]
    dj = [-1,0,1, -1,1, -1,0,1]

    for i in range(L):
        for j in range(L):
            if seat[i][j] == 'C':  # C찾고
                cnt = 1
                while cnt < 4:
                    for n in range(8):
                        new_i = i + di[n]*cnt
                        new_j = j + dj[n]*cnt
                        x = abs(i - new_i)
                        y = abs(j - new_j)
                        # 인덱스 and 방문했는지
                        if 0 <= new_i < L and 0 <= new_j < L and visited[new_i][new_j] == 0:

                            if seat[new_i][new_j] == 'M' and x + y <= 2:
                                answer += 1
                                visited[new_i][new_j] = 1  # 방문체크해주고
                            elif seat[new_i][new_j] == 'N' and x + y <= 3:
                                answer += 1
                                visited[new_i][new_j] = 1  # 방문체크해주고
                    cnt += 1
    print(answer)
    return answer


def solution2(seat):
    # print(seat)
    answer = 0
    L = len(seat)
    visited = [[0] * L for _ in range(L)]
    check = []
    for i in range(L):
        for j in range(L):
            if seat[i][j] == 'C':  # C찾고
                check.append([i, j])
    for i in range(L):
        for j in range(L):

            if seat[i][j] == 'M' and visited[i][j] == 0:  # M찾고
                for m in check:
                    if abs(i - m[0]) + abs(j - m[1]) <= 2:
                        answer += 1
                        visited[i][j] = 1
                        break
            elif seat[i][j] == 'N' and visited[i][j] == 0:  # N찾고
                for n in check:
                    if abs(i - n[0]) + abs(j - n[1]) <= 3:
                        answer += 1
                        visited[i][j] = 1
                        break
    print(answer)
    return answer
seat = ["M--NN-", "-M----", "-CC--M", "-N----", "N-M-C-", "-M----"]
# seat = 	["CMMM", "NNNN", "MMMM", "NNNN"]
solution2(seat)