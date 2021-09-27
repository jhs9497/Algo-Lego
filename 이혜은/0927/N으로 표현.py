def solution(N, number):
    answer = 0
    # nums: 인덱스 번호에 인덱스 번호 만큼의 수를 사용하여 만들 수 있는 수들의 리스트를 저장
    nums = [[]] 
    
    def make_num():
        print(nums)
        for i in range(1, 9):
            # 최소한 1개 최대 8개까지 가능
            tmp_lst = []
            # 이미 만들어진 수를 조합해서 만드는 경우
            for j in range(1, i):
                for k in nums[j]:
                    for l in nums[i-j]:
                        # 더하기
                        tmp_lst.append(k+l)
                        # 빼기
                        if k-l >= 0:
                            tmp_lst.append(k-l)
                        # 곱하기
                        tmp_lst.append(k*l)
                        # 나누기
                        if k != 0 and l != 0:
                            tmp_lst.append(k//l)
            # 수들이 연속적으로 나올 수 있음(ex. 555)
            tmp_lst.append(int(str(N)*i))
            # 만일 i개를 이용하여 만든 수들의 배열 안에 찾는 숫자가 있다면 i리턴
            if number in tmp_lst:
                return i
            nums.append(list(set(tmp_lst)))

        # 8까지 돌아본 후에도 없다면 -1 리턴
        return -1

    answer = make_num()
    return answer