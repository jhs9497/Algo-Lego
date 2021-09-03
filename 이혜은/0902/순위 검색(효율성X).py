def solution(info, query):
    # info 지원자 데이터 / query: 체크할 데이터
    
    answer = []
    
    for data in query:
        
        ans = 0
        want = list(data.split())
        want_info = []
        
        for one_want in want:
            if one_want != 'and':
                want_info.append(one_want)
        
        for student in info:
            student_info = list(student.split())
            
            stop = False

            for i in range(5):
                if want_info[i] == '-':
                    continue
                if i < 4 and want_info[i] != student_info[i]:
                    stop = True
                    break
                if i == 4 and int(want_info[i]) > int(student_info[i]):
                    stop = True
                    break
            
            if not stop:
                ans += 1
                
        answer.append(ans)
        
    return answer

info = [["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
# result = [1,1,1,1,2,4]

solution(info, query)