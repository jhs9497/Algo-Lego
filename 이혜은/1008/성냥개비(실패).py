lst = [[] for _ in range(101)]
tmp_lst = [i for i in range(10)]
nums = {'1': 2, '2': 5, '3': 5, '4': 4, '5': 5, '6': 6, '7': 3, '8': 7, '9': 6, '0': 6}

for num in nums:
    lst[nums[num]].append(int(num))

print(lst)

# 1, 8, 9 개에 대한 정보 X
import sys
n = int(sys.stdin.readline())

for _ in range(n):
    n = int(sys.stdin.readline())
    def solution(n):

        for i in range(2, n):
            for j  in range(2, i+1):
                for l in lst[i]:
                    for k in lst[j]:
                        tmp = str(l) + str(k)
                        if tmp[0] != '0':
                            lst[i+j].append(int(tmp))
                        
                        tmp = str(k) + str(l)
                        if tmp[0] != '0':
                            lst[i+j].append(int(tmp))

                        tmp = str(l) + str(l)
                        if tmp[0] != '0':
                            lst[i+i].append(int(tmp))

            print(lst)     
        print(min(lst[n]), max(lst[n]))
        
        
    solution(n)

# n = 4
# (3) # 7 7
# (6) # 6 111
# (7) # 8 711
# (15) #108 7111111


