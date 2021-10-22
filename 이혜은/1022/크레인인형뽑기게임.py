ans = 0

def solution(board, moves):
    
    result = []
    
    new_board = [[0]*len(board) for _ in range(len(board))]
    
    for i in range(len(board)):
        for j in range(len(board)):
            # (0, 0)(0, 1)(0, 2) ... (4, 4)(3, 4)(2, 4)
            new_board[len(board)-i-1][j] = board[len(board)-j-1][len(board)-i-1]
    
    board = new_board
    
    def check():
        
        global ans
        
        N = len(result)-1
        
        if N < 1:
            return
        
        if result[N] == result[N-1]:
            result.pop()
            result.pop()
            ans += 2
            
        N = len(result)-1
        
        if N < 1:
            return
        
        if result[N] == result[N-1]:
            check()
            
    
    def delete(lst):
        
        if lst[0] == 0:
            return 
        
        for i in range(len(lst)):
            if i == len(lst)-1 or i+1 < len(lst) and lst[i+1] == 0:
                result.append(lst[i])
                lst[i] = 0
                return 
    
    for move in moves:
        delete(board[move-1])
        check()
        
    
    
    return ans