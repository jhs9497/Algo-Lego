def match(arr, key, rot, r, c, n, offset):
    n = len(key)
    for i in range(n):
        for j in range(n):
            if rot == 0:
                arr[r+i][c+j] += key[i][j]
            elif rot == 1:
                arr[r+i][c+j] += key[n-1-j][i]
            elif rot == 2:
                arr[r+i][c+j] += key[n-1-i][n-1-j]
            else:
                arr[r+i][c+j] += key[j][n-1-i]
            if offset <= r+i < offset + n and offset <= c+j < offset + n:
                if arr[r+i][c+j] != 1:
                    return False
    return True
            
def check(arr, offset, n):
    for i in range(n):
        for j in range(n):
            if arr[offset+i][offset+j] != 1:
                return False
    return True
    
def solution(key, lock):
    answer = False
    offset = len(key) - 1
    
    for i in range(offset + len(lock)):
        for j in range(offset + len(lock)):
            for rot in range(4):
                arr = [[0 for _ in range(60)] for _ in range(60)]
                for k in range(len(lock)):
                    for z in range(len(lock)):
                        arr[offset + k][offset + z] = lock[k][z]
                if match(arr, key, rot, i, j, len(lock), offset):
                    answer = True
                    print(answer)
                    break
            if answer:
                break
        if answer:
            break
                # if check(arr, offset, len(lock)):
                #     return True
    return answer