from itertools import combinations


def solution(orders, course):
    answer = []
    menu_list = [set() for _ in range(course[-1] + 1)]
    for i in range(len(orders)):
        tmp_list = []
        for j in range(len(orders[i])):
            tmp_list.append(orders[i][j])

        for a in course:
            if a <= len(tmp_list):
                combi_list = combinations(tmp_list, a)
                combi_list = list(combi_list)
                for b in combi_list:
                    b = list(b)
                    b = sorted(b)
                    menu = "".join(b)
                    menu_list[a].add(menu)

    for i in range(len(menu_list)):
        menu_list[i] = list(menu_list[i])
        menu_list[i].sort()

    # 여기까지 요러한 갯수별 조합 리스트 만들기
    # [[], [], ['AB', 'AC', 'AD', 'AE', 'AF', 'AG', 'AH', 'BC', 'BF', 'BG', 'CD', 'CE', 'CF', 'CG',
    # 'CH', 'DE', 'DH', 'EH', 'FG'], ['ABC', 'ABF', 'ABG', 'ACD', 'ACE', 'ACF', 'ACG', 'ACH', 'ADE',
    # 'ADH', 'AEH', 'AFG', 'BCF', 'BCG', 'BFG', 'CDE', 'CDH', 'CEH', 'CFG', 'DEH'], ['ABCF', 'ABCG',
    # 'ABFG', 'ACDE', 'ACDH', 'ACEH', 'ACFG', 'ADEH', 'BCFG', 'CDEH']]

    for a in range(len(menu_list)):
        count_list = [0] * len(menu_list[a])
        for b in range(len(menu_list[a])):
            total_count = 0
            for order in orders:
                count = 0
                for single_menu in menu_list[a][b]:
                    if order.find(single_menu) > -1:
                        count += 1

                if count == len(menu_list[a][b]):
                    total_count += 1

            if total_count >= 2:
                count_list[b] = total_count

        # 여기까지 갯수별 조합리스트의 카운팅횟수 만들기
        # []
        # []
        # [0, 4, 2, 2, 0, 0, 0, 2, 2, 2, 3, 3, 2, 2, 0, 3, 0, 0, 2]
        # [0, 0, 0, 2, 2, 0, 0, 0, 2, 0, 0, 0, 2, 2, 2, 3, 0, 0, 2, 0]
        # [0, 0, 0, 2, 0, 0, 0, 0, 2, 0]

        max_count = 2
        for i in count_list:
            if max_count < i:
                max_count = i
        # 각 리스트에서 2이상의 max_count를 구한 후 max_count와 일치하는 경우 answer에 append
        for j in range(len(count_list)):
            if max_count == count_list[j]:
                answer.append(menu_list[a][j])
    answer.sort()

    return answer