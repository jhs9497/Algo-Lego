def solution(s):
    entire_list = []
    s = s[1:-1]
    number = ''
    number_list = []
    flag = False
    for e in s:
        if e == '{':
            flag = True
        elif flag == True and e.isdigit():
            number += e
        elif flag == True and e == ',':
            number_list.append(number)
            number = ''
        elif e == '}':
            number_list.append(number)
            entire_list.append(number_list)
            number_list = []
            number = ''
            flag = False

    entire_list.sort(key=lambda x: len(x))

    answer = []
    for i in range(len(entire_list)):
        for j in range(len(entire_list[i])):
            if int(entire_list[i][j]) not in answer:
                answer.append(int(entire_list[i][j]))
                break

    return answer