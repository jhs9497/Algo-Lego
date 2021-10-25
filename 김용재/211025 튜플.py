def solution(s):
    arr = []
    answer = []
    word = ''
    for i in range(1, len(s) - 1):

        if s[i] == '{':
            flag = True
            pass

        elif flag == True and s[i] == ',':  # 괄호안에있는 ,
            arr.append(int(word))
            word = ''  # 초기화
            pass

        elif s[i] == '}':
            flag = False
            if s[i + 1] == '}':
                # print(word,'ddd')
                arr.append(int(word))
                word = ''  # 초기화

        elif flag == False and s[i] == ',':  # 괄호밖에 있는 ,
            arr.append(int(word))
            word = ''  # 초기화
            pass

        else:
            # print(s[i])
            word += s[i]

    # print(arr)

    arr_set = set(arr)
    # print(arr_set)

    answer_dict = {}

    for s in arr_set:
        cnt = arr.count(s)
        answer_dict[s] = cnt
    # print(answer_dict)

    sorted_dict = sorted(answer_dict.items(), key=lambda item: item[1], reverse=True)
    #     print(sorted_dict[0][0])
    #     print(len(sorted_dict))

    for key in range(len(sorted_dict)):
        # print(sorted_dict[key][0])
        answer.append(sorted_dict[key][0])
    return answer
s = "{{2},{2,1},{2,1,3},{2,1,3,4}}"
print(solution(s))