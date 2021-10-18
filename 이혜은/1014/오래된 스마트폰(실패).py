#  ‘+’는 1, ‘-‘는 2, ‘*’는 3, ‘/’는 4로 
tmp_lst_2 = []
for test in range(int(input())):
    
    answer = -1

    N, O, M = map(int, input().split())
    nums = list(map(int, input().split()))
    methohs = list(map(int, input().split()))

    res = int(input())
    tmp_lst = [[]]

    def make_num(n, tmp_n):

        if tmp_n and int(tmp_n) > 999:
            return

        if len(tmp_n) == n:
            tmp.append(int(tmp_n))
            return 

        for num in nums:
            make_num(n, tmp_n+str(num))

    for i in range(1, M+1):
        tmp = []
        make_num(i, "")
        print(i, tmp)
        tmp_lst.append(list(set(tmp)))
        for j in range(1, i):
            for k in tmp_lst[j]:
                for l in tmp_lst[i-j]:
                    if 1 in methohs:
                        tmp.append(k+l)
                    if 2 in methohs and l-k >= 0:
                        tmp.append(l-k)
                    if 3 in methohs:
                        tmp.append(l*k)
                    if k != 0 and 4 in methohs:
                        tmp.append(l//k)

        tmp_lst_2 = []
        print(tmp)

        tmp_lst.append(list(set(tmp)))
        if res in tmp:
            answer = i
            print("ans", answer)
            break
    print(tmp_lst)
    if answer == -1:
        print("ans", -1)
    

