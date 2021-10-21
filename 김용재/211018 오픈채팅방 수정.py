def solution(record):
    dic = {}
    answer = []


    for tc in record:
        word = list(map(str, tc.split()))
        if len(word) > 2:  # Leave빼고 나머지
            userid = word[1]
            nickname = word[2]
            dic[userid] = nickname
    for tc in record:
        word = list(map(str, tc.split()))
        command = word[0]
        userid = word[1]
        if command == 'Enter':
            answer.append(dic[userid] + '님이 들어왔습니다.')
        elif command == 'Leave':
            answer.append(dic[userid] + '님이 나갔습니다.')

    return answer