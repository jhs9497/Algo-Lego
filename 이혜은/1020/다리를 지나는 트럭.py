from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    sumT = 0
    
    bridge = deque()
    for _ in range(bridge_length):
        bridge.append(0)
    
    for truck_weight in truck_weights:
        
        if sumT + truck_weight > weight:
            while sumT + truck_weight > weight:
                sumT -= bridge.popleft()
                if sumT + truck_weight <= weight:
                    break
                bridge.append(0)
                answer += 1
            bridge.append(truck_weight)
            sumT += truck_weight
            answer += 1
        else:
            sumT -= bridge.popleft()
            bridge.append(truck_weight)
            sumT += truck_weight
            answer += 1
    
    return answer+bridge_length