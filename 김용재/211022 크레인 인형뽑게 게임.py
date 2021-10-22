def solution(board, moves):
    answer = 0
    basket = []
    for _ in range(len(moves)):
        j = moves.pop(0) - 1

        for i in range(len(board)):
            if board[i][j] == 0:
                pass
            else:  # 숫자가 있으면
                pick = board[i][j]
                basket.append(pick) # 바구니에 넣음
                board[i][j] = 0
                print(pick)

                if len(basket) > 1:  # 바구니가 2개 이상이면
                    if basket[-1] == basket[-2]:  # 같으면
                        answer += 2  # 답 두개 추가하고
                        basket.pop(-1)  # 한개씩 뺌
                        basket.pop(-1)
                        print(basket)
                break

    return answer
board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
print(solution(board, moves))