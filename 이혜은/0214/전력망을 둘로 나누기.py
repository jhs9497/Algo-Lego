def solution(n, wires):
    answer = 0x9999999999999
    
    def find_ans(i):
        
        visited = [False]*(n+1)
        visited[1] = True
        s = [1]
        tmp = 0
        while s:
            point = s.pop()
            for j in range(len(wires)):
                if j == i:
                    continue
                if wires[j][0] == point and not visited[wires[j][1]]:
                    visited[wires[j][1]] = True
                    s.append(wires[j][1])
                if wires[j][1] == point and not visited[wires[j][0]]:
                    visited[wires[j][0]] = True
                    s.append(wires[j][0])
                    
        tmp = 0
        for i in range(1, len(visited)):
            if visited[i]:
                tmp += 1
        k = n - tmp  
        
        return (k-tmp)
    
        
    for i in range(len(wires)):
        tmp = abs(find_ans(i))
        if tmp < answer:
            answer = tmp
        
    return answer