from itertools import combinations


def solution(user_id, banned_id):
    answer = 0
    answer_list = []
    check = [[] for _ in range(len(banned_id))]
    # print(check)

    for user in user_id:
        for i in range(len(banned_id)):
            # 우선 길이가 같아야함
            if len(user) == len(banned_id[i]):
                cnt = 0
                for j in range(len(banned_id[i])):  # 글자마다 체크
                    if banned_id[i][j] == '*':  # 별표면 pass
                        cnt += 1
                    else:  # 아니면 체크
                        if banned_id[i][j] == user[j]:  # 글자 같으면
                            cnt += 1
                        else:  # 글자 다르면
                            break
                if cnt == len(banned_id[i]):  # 글자 전부 같으면
                    check[i].append(user)  # user 추가


            else:  # 길이 다르면
                pass
    print(check)
    visited = [[False] * len(check[i]) for i in range(len(check))]

    def dfs(i, j):
        stack = []
        stack.append(i)
        visited[i][j] = True
        while stack:
            i = stack.pop(-1)
            for idx in range(len(check[i])):
                if check[i][idx] not in answer_list and visited[i][idx] == False:
                    visited[i][idx] = True
                    stack.append(check[i][idx])


    for i in range(len(check)):
        for j in range(len(check[i])):
            if visited[i][j] == False:
                dfs(i, j)

    return answer

user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id = ["fr*d*", "abc1**"]
solution(user_id, banned_id)