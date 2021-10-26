def solution(bridge_length, weight, truck_weights):
    ans = 0
    road = []
    i = 0
    
    while i < len(truck_weights):
        print('here', i)
        road = [truck_weights[i]]
        flag = False
        tmp = 0
        while i < len(truck_weights)-1 and len(road)+1 <= bridge_length and sum(road)+truck_weights[i+1]<=weight:
            road.append(truck_weights[i+1])
            tmp += 1
            i += 1
            print('flag', road, i, tmp)
            flag = True
        i += 1
        ans += tmp + bridge_length
        
    return ans + 1