def solution(triangle):
    
    tmp_lst = [[-1]*(i+1) for i in range(len(triangle))]
    tmp_lst[0][0] = triangle[0][0]
    
    def down(nr, nc):
        
        if nr == len(triangle):
            return
        
        if nr == 0:
            tmp_lst[nr][nc] == triangle[nr][nc]
        
        else:
            for i in range(nr+1):
                if i == 0:
                    tmp_lst[nr][i] = tmp_lst[nr-1][0] + triangle[nr][0]
                elif i == nr:
                    tmp_lst[nr][i] = tmp_lst[nr-1][nr-1] + triangle[nr][nr]
                else:
                    if tmp_lst[nr-1][i-1] > tmp_lst[nr-1][i]:
                        tmp_lst[nr][i] = tmp_lst[nr-1][i-1] + triangle[nr][i]
                    else:
                        tmp_lst[nr][i] = tmp_lst[nr-1][i] + triangle[nr][i]
                    
        down(nr+1, 0)

    down(0, 0)
    tmp = tmp_lst[len(tmp_lst)-1]
    print(tmp_lst)

    return max(tmp)