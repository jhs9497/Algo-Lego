# 2021 KAKAO BLIND RECRUITMENT

def add_menu(menu_lst, course, max_course, combo, start):
    
    # menu_lst: 각각의 메뉴를 리스트화 한것, course, max_course, combo: 경우의 수, start: 경우의 수 중복을 막기 위한 start 변수(for문에 사용)
    if len(combo) > max_course:
        return
    
    global menues
    
    if len(combo) in course:
        # combo: String => sorted를 사용해 중복 제거
        combo = "".join(sorted(list(combo)))
        
        if combo in menues:
            menues[combo] += 1
        else:
            menues[combo] = 1
            
    for i in range(start, len(menu_lst)):
        add_menu(menu_lst, course, max_course, combo+menu_lst[i], i+1)
    
    
menues = {}
def solution(orders, course):
    global menues
    answer = []
    max_course = max(course)
    
    for order in orders:
        menu_lst = list(order)
        add_menu(menu_lst, course, max_course, '', 0)
    
    # menues 안의 모든 경우의 세트 메뉴에서 각각의 course 값의 최대값을 구하기 위한 이차원배열
    # [주문 수, 주문 경우] ex. [2, 'AC']
    ans = [[-1, ''] for _ in range(max_course+1)]
    
    for menu in menues:
        long = len(menu)
        if ans[long][0] < menues[menu] and menues[menu] > 1:
            ans[long][0] = menues[menu]
            ans[long][1] = menu
        # 메뉴의 수가 같은 경우 함께 출력 필요 => /와 함께 문자열 저장
        elif ans[long][0] == menues[menu] and menues[menu] > 1:
            ans[long][1] += '/' + menu
            
    for i in course:
        all = ans[i][1]
        tmp = all.split('/')
        for t in tmp:
            if t:
                answer.append(t)
                
    answer.sort()
    
    
    
    return answer