# 중복 정답을 제거하기 위해 set사용
answer_set = set()

def solution(user_id, banned_id):

    # visited 체크. 사용자가 불량 사용자로 체크 되었는지를 idx로 확인
    checked = [0] * len(user_id)
    
    # 불량 사용자 확인
    def find_user(num, i):
        
        global answer_set
    
        # 만일 불량 사용자를 다 찾았다면
        if num == len(banned_id):
            # checked의 값을 문자열로 저장해 set에 add
            ans = "".join(map(str, checked))
            answer_set.add(ans)
            return

        # 만일 인덱스 위치를 벗어난다면 return
        if i > len(banned_id)-1:
            return
        
        # 이번에 찾을 제재 아이디
        ban_id = banned_id[i]
        
        # 유저를 돌며
        for k in range(len(user_id)):
            # 아직 제재 리스트에 추가되지 않고
            if checked[k]:
                continue
            # 제재 아이디와 유저의 이름의 길이가 다르지 않은 사용자 중에서
            if len(ban_id) != len(user_id[k]):
                continue
            t = 0
            correct = True
            # 별을 제외하고 다른 문자가 겹치는지를 확인
            while t < len(ban_id):

                if ban_id[t] == '*':
                    t += 1
                    continue

                if ban_id[t] != user_id[k][t]:
                    correct = False
                    break

                t += 1
            # 만일 가능한 사용자라면
            if correct:
                # 체크리스트에 표기해서
                checked[k] = 1
                # 다음 제재 아이디를 확인
                find_user(num+1, i+1)
                # 체크리스트는 원래로 돌리기
                checked[k] = 0
                    
    
    find_user(0, 0)
    
    return len(answer_set)