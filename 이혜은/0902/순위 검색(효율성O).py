from itertools import combinations
from collections import defaultdict
# dict안에 key값이 존재하는지 안하는지를 굳이 확인안해주고 진행 가능 -> int면 0, set이면 set을 기본값으로

def solution(infos, queries):
    
    answer = []
    student_dict = defaultdict(list)
    
    for info in infos:
        info = info.split()
        score = int(info[-1])
        conditions = info[:4]
        # conditions = info[:-1]
        
        for i in range(5):
            # tmps = list(combinations(conditions, i))
            for tmp in combinations(conditions, i):
                student = ''.join(tmp)
                student_dict[student].append(score)
    
    for key in student_dict.keys():
        student_dict[key].sort()
        
    for query in queries:
        query_str = ''
        tmp_lst = query.split()
        score = int(tmp_lst[-1])
        # tmp_lst = tmp_lst[:-1]

        for tmp_info in tmp_lst[:7]:
            if tmp_info != '-' and tmp_info != 'and':
                query_str += tmp_info
                
#         for i in range(3):
#             tmp_lst.remove('and')
#         while '-' in tmp_lst:
#             tmp_lst.remove('-')
            
        # query_str = ''.join(tmp_lst)

        if query_str in student_dict:
            scores = student_dict[query_str]
            start, end = 0, len(scores)
            while end > start:
                mid = (start + end) // 2
                if scores[mid] >= score:
                    end = mid
                else:
                    start = mid + 1
            
        
            answer.append(len(scores) - start)
        else:
            answer.append(0)
        
    return answer