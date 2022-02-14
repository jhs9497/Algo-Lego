def solution(n):
    board = [[0] * n for _ in range(n)]
    answer = []
    x, y = -1, 0
    num = 1

    for i in range(n):
        for _ in range(i, n):
            # down
            if i % 3 == 0:
                x += 1

            # right
            elif i % 3 == 1:
                y += 1

            # up
            elif i % 3 == 2:
                x -= 1
                y -= 1

            board[x][y] = num
            num += 1

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] != 0:
                answer.append(board[i][j])

    return answer