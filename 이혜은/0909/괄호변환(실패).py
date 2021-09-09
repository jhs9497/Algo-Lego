def change(u, v):
        
    tmp_u = ''
    for i in range(1, len(u)-1):
        if u[i] == '(':
            tmp_u += ')'
        else:
            tmp_u += '('
    
    return '(' + v + ')' + tmp_u

def check(p):
    
    if len(p) == 0:
        return True
    
    tmp = 0
    flag = True
    
    for i in range(len(p)):
        if p[i] == '(':
            tmp += 1
        else:
            tmp -= 1
        
        if tmp < 0:
            flag = False
            
    return flag

def check_p(p, ans):

    i = 0
    tmp = 0

    while i < len(p):

        j = 0
        u = ''; v = '';

        while (i+j) < len(p):
            if p[i+j] == '(':
                tmp += 1
                u += '('
            else:
                tmp -= 1
                u += ')'

            if tmp == 0:
                break

            j += 1
        

        i += j+1
        
        if i < len(p):
            v = p[i:]
        else:
            v = ''
        # print(u, v)
        u_tmp = 0
        u_flag = check(u)

        if u_flag:
            ans += u
            check_p(v, ans)
        else:
            ans += change(u, v)
            
    return ans

def solution(p):
    # 개수만 맞는다면 : 균형잡힌 괄호 문자열 / 다 맞는다면 : 올바른 괄호 문자열
    
    answer = ''
    
    flag = check(p)
    
    if flag == False:
        answer += check_p(p, '')
    else:
        answer = p
            
    return answer