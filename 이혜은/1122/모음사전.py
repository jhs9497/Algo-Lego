tmp = 0
find = False

def solution(find_word):
    answer = 0
    alphas = ['A', 'E', 'I', 'O', 'U']
    words = []
    
    def make_words(word):
        
        global tmp
        global find
        
        if word == find_word:
            find = True
            return 
        
        if find:
            return
        
        if word == '':
            pass
        else:
            words.append(word)
            tmp += 1
        
        if len(word) >= 5:
            return
        
        for i in range(len(alphas)):
            make_words(word+alphas[i])
            # '' => make_words('A') / make_words('E') / make_words('I')  ...
    
    make_words('')
    
    return tmp+1