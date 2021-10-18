def solution(record):
    nickname_dict = {}
    for info in record:
        info_list = list(info.split())
        if info_list[0] == 'Enter' or info_list[0] == 'Change':
            nickname_dict[info_list[1]] = info_list[2]

    answer = []
    for info in record:
        info_list = list(info.split())
        if info_list[0] == 'Enter':
            answer.append(nickname_dict[info_list[1]] + '님이 들어왔습니다.')
        elif info_list[0] == 'Leave':
            answer.append(nickname_dict[info_list[1]] + '님이 나갔습니다.')

    return answer