def solution(records):
    answer = []
    
    users = {}
    for record in records:
        tmp = list(record.split())
        if len(tmp) > 2:
            do, user, username = map(str, tmp)
            users[user] = username
    
    for record in records:
        tmp = list(record.split())
        if len(tmp) > 2:
            if tmp[0] == "Enter":
                answer.append(users[tmp[1]]+'님이 들어왔습니다.')
        else:
            answer.append(users[tmp[1]]+'님이 나갔습니다.')
            
        
    return answer