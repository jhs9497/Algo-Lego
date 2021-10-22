def solution(board, moves):
    answer = 0
    result = []
    
    for move in moves:
        
        for i in range(len(board)):
            if board[i][move-1] != 0:
                result.append(board[i][move-1])
                board[i][move-1] = 0
                N = len(result)-1
                if N < 1:
                    break
                if result[N] == result[N-1]:
                    result.pop()
                    result.pop()
                    answer += 2
                    break
                break
        
    return answer