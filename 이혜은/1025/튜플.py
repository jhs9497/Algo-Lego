def solution(s):

    # 정답을 담은 배열
    ans = []

    # 넉넉한 길이의 임시 배열 생성
    tmp_lst = [-1]*(len(s))
    # 집합 단위로 나누어 리스트로 저장
    lst = s.split('},{')
    
    # 집합 단위로 데이터를 보면서
    for data in lst:
        tmp = ''
        # 데이터 안의 문자가
        for i in data:
            # 괄호라면 continue
            if i == '{' or i == '}':
                continue
            # 아니라면 tmp에 추가
            tmp += i
        # tmp는 다시 ,단위의 리스트로 나누어 몇 개의 원소로 이루어진 집합인지 확인
        tmp = list(tmp.split(','))
        # 사용한 원소 개수 위치에 tmp 저장
        tmp_lst[len(tmp)] = tmp
    
    # tmp_lst를 돌면서(0개째는 확인 X)
    for i in range(1, len(tmp_lst)):
        # 만약 원소 개수를 넘어가는 공간이 나온다면 break
        if tmp_lst[i] == -1:
            break
        # 아니라면 원소를 하나씩 보며
        for j in tmp_lst[i]:
            #  만일 원소가 정답 배열에 있다면 continue
            if int(j) in ans:
                continue
            # 아니라면 정답 배열에 추가
            ans.append(int(j))
            # 만일 원소의 개수가 i개가 되었다면 break
            if len(ans) == i:
                break
            
    return ans