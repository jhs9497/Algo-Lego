from collections import defaultdict

def solution(files):
    file_dict = defaultdict(list)
    answer = []
    sort_arr = []
    
    for file in files:
        if file.find(".") > -1:
            HEAD, TAIL = file.split(".")
        else:
            HEAD = file

        NUMBER = ""
        idx = 0
        for i in range(len(HEAD)):
            if HEAD[i].isdigit():
                NUMBER += HEAD[i]
                if idx == 0:
                    idx = i
        
        HEAD = HEAD[0:idx]
        HEAD = HEAD.lower()
        
        NUMBER = str(int(NUMBER))
        
        KEY = HEAD + NUMBER
    
        file_dict[KEY].append(file)        
        
        sort_arr.append((HEAD, int(NUMBER)))
    
    
    sort_arr = set(sort_arr)
    sort_arr = list(sort_arr)

    sort_arr.sort()
    
    for value in sort_arr:
        key = value[0] + str(value[1])
        for file in file_dict[key]:
            answer.append(file)

    return answer