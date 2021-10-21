from copy import deepcopy
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    arr2 = deepcopy(arr)
    # print(arr)
    answer = 0
    # 포의 현재위치 찾기
    current = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                current.append([i,j])
                break
    # current.pop(1) # 앞에께 빠짐
    print(current)
    #
    # 현재 위치 기준으로 상하좌우 (-1,+1,-1,+1)
    num = [[-1,0] ,[+1,0], [0,-1], [0,+1]]
    # 제일 가까운 상하좌우 알 찾기
    back = len(current) # 나중에 앞에꺼 지우려고

    def three(answer, back, t):
        arr = arr2
        for c in range(back): # 이 부분을 3번 반복해야한다.
            i = current[c][0]
            j = current[c][1]
            # 이때 원래의 2 위치가 현재 위치로 옮겨졌다는 걸 알려줘야함
            arr[i][j] = 2
            # 원래있던 2는 0 으로 바꿔줘야함
            if t > 0:
                arr[3][2] = 0

            for n in num:
                cnt = 0
                new_i = i + n[0]
                new_j = j + n[1]

                while cnt < 2 and  0<= new_i < N and 0<= new_j < N: # 2개만나기 전 and 장기판 안
                    if cnt == 0 and arr[new_i][new_j] == 1: # 첫번째 알이면
                        cnt += 1
                        new_i += n[0]
                        new_j += n[1]

                    elif cnt == 0 and arr[new_i][new_j] == 0: # 만나기 전 빈공간이면
                        new_i += n[0]
                        new_j += n[1]

                    elif cnt == 1 and arr[new_i][new_j] == 1: # 두번째 알이면
                        if [new_i, new_j] not in current:
                            current.append([new_i, new_j])  # 다음번에 갈 곳 추가
                            answer += 1  # 정답에 추가
                        cnt += 1
                        new_i += n[0]
                        new_j += n[1]



                    elif cnt == 1 and arr[new_i][new_j] == 0:# 첫번째 이후 빈공간
                        if [new_i, new_j] not in current:
                            current.append([new_i, new_j])  # 다음번에 갈 곳 추가
                        new_i += n[0]
                        new_j += n[1]
            # x = current[c][0]
            # y = current[c][1]
            # arr[x][y]= 0

        for b in range(back):
            # arr[current[b][0]][current[b][1]] = 0 # 쓴자리는 다시 0으로 돌려줌
            current.pop(b)
        return answer

    for t in range(3):
        answer = three(answer, len(current), t)
        print(answer)