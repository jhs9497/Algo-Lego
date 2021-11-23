from itertools import combinations

def solution(relation):
    answer = 0
    arr = []
    check = [0] * len(relation[0])
    print(check)
    for i in range(len(relation[0])):
        for j in range(len(relation)):
            print(j,i)
            if relation[j][i] in arr:
                check[i] = 1
                arr = []
                break
            else:
                arr.append(relation[j][i])
            print(arr)
            print(check,'check')
        print(arr)
        print(check)
        if len(arr) == len(relation[0]) and len(set(arr)) == len(arr):  # 중복 없으면
            check[i] = 0
            arr = []

    print(arr)
    print(check)

    for i in range(len(relation[0])):
        comb(i, check)

    return answer
def comb(i):
    list(combinations(relation, 2))


relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]
solution(relation)
