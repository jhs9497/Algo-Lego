answer = 0

def solution(m, n, board):
    
    def find(m, n, board):
        
        global answer
        delete = set()

        for i in range(m):
            for j in range(n):
                if board[i][j] == '0':
                    continue
                if i >= m-1 or j >= n-1:
                    continue
                if board[i][j] == board[i][j+1] == board[i+1][j] == board[i+1][j+1]:
                    delete.add((i, j))
                    delete.add((i, j+1))
                    delete.add((i+1, j))
                    delete.add((i+1, j+1))

        answer += len(delete)

        tmp_lst = []

        for i in range(n):
            tmp = []
            for j in range(m):
                if (j, i) in delete:
                    continue
                else:
                    tmp.append(board[j][i])
            tmp = ['0'] * (m-len(tmp)) + tmp
            tmp_lst.append(tmp)

        new_board = []
        for i in range(m):
            tmp = ""
            for j in range(n):
                tmp += tmp_lst[j][i]
                # 0, 4 / 1, 4 ... 4, 4 // 0, 0 / 1, 0 ... 4, 0           
            new_board.append(tmp)

        board = new_board
        stop = True
        for i in range(m):
            for j in range(n):
                if board[i][j] == '0':
                    continue
                if i >= m-1 or j >= n-1:
                    continue
                if board[i][j] == board[i][j+1] == board[i+1][j] == board[i+1][j+1]:
                    stop = False

        if stop:
            return
        else:
            find(m, n, board)
            
    find(m, n, board)
    
    return answer