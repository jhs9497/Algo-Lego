def solution(record):

    answer = []
    check = []
    inout = []

    for tc in record:

        word = list(map(str, tc.split()))
        command = word[0]

        if command == 'Enter':
            userid = word[1]
            nickname = word[2]

            for idx in range(len(check)):
                if check[idx][0] == userid:
                    check[idx][1] = nickname

            check.append([userid, nickname])
            inout.append('님이 들어왔습니다.')

        elif command == 'Leave':
            userid = word[1]
            for c in check:
                if c[0] == userid:
                    nickname = c[1]
            check.append([userid, nickname])
            inout.append('님이 나갔습니다.')

        elif command == 'Change':
            userid = word[1]
            nickname = word[2]
            for c in check:
                if c[0] == userid:
                    c[1] = nickname
    print(check)
    print()
    print(inout)
    print()

    for a in range(len(check)):
        answer.append(check[a][1] + inout[a])

    print(answer)

    return answer