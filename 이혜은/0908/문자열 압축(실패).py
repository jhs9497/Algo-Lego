def solution(s):
    answer = len(s)
    
    for i in range(1, len(s)//2+1):
        
        ans = ''
        
        j = 0
        tmp = 1
        tmp_s = ''
        
        while j < len(s):
            print(i, j)
            if s[j:j+i] == s[j+i:j+2*i]:
                tmp += 1
                tmp_s = s[j:j+i]
                j = j+i
            else:
                print('there', tmp_s, tmp)
                if tmp != 1:
                    j += len(tmp_s) - 1
                    ans += str(tmp) + tmp_s
                else:
                    ans += s[j]
                tmp = 1
                tmp_s = ''
                j += 1
        if len(ans) < answer:
            answer = len(ans)
            
    return answer