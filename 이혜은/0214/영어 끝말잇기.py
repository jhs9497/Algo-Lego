def solution(n, words):
    answer = []
    word_dict = {}
    
    i = 1
    who = 0
    last_word = ''
    
    for word in words:
        if word in word_dict:
            break
        elif last_word != '' and word[0] != last_word:
            break
        else:
            word_dict[word] = 1
            last_word = word[-1]
        i += 1
        who += 1
        if who == n:
            who = 0
    
    if len(words) < i:
        return [0, 0]
    else:
        if not i % n:
            return [who+1, i//n]
        else:
            return [who+1, i//n + 1]
    
    return answer