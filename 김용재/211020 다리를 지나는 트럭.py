def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = [0] * bridge_length

    while bridge:
        answer += 1
        bridge.pop(0)
        if truck_weights:
            if sum(bridge) + truck_weights[0] <=weight:
                bridge.append(truck_weights.pop(0))
            else:
                bridge.append(0)




    # while truck:
    #     if sum(bridge) + truck[0] <= weight:  # 무게가 꽉 안찼으면
    #         T = truck.popleft()  # 트럭 앞에 빼고
    #         if len(bridge) <= bridge_length:  # 다리길이 봐서 아직 ㄱㅊ으면
    #             bridge.append(T)  # 트럭 넘김
    #             answer += 1  # 넘겼으니 1초 추가
    #         else:  # 다리길이 꽉찼으면
    #             bridge.popleft()  # 통과시켜주고
    #             answer += 1  # 1초 추가
    #
    #     else:  # 무게 꽉찼으면
    #         # if bridge_length == len(bridge):
    #         #     answer += 1
    #         # else:
    #         #     answer += bridge_length  # 1초 추가
    #         bridge.popleft()  # 통과시켜주고
    #         answer += bridge_length
    #         T = truck.popleft()
    #         bridge.append(T)
    # answer += bridge_length
    return answer


bridge_length = 2
weight = 10
truck_weights = [7,4,5,6]
#
# bridge_length = 100
# weight = 100
# truck_weights = [10]
# 100	100	[10]	101
# 100	100	[10,10,10,10,10,10,10,10,10,10]	110
print(solution(bridge_length, weight, truck_weights))