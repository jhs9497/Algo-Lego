from collections import deque

def solution(bridge_length, weight, truck_weights):
    B = [0] * bridge_length  # 길이가 2인 다리 표현
    B = deque(B)
    sumB = 0 # 다리위의 총무게를 나타내는 변수, 시간초과때문에 사용
    W = weight  # 10
    sec = 0 # 초
    truck = deque(truck_weights)  # 시간 초과가 떠서 deque활용

    while len(truck) > 0: # deque로 받은 트럭이 다 건너기 전까지

        sec += 1  # while문 한 번 돌때마다 1초씩 추가
        if sumB <= W:  # 만약 다리위의 트럭 총합이 W보다 낮을때
            sumB -= B[0]
            B.popleft()
            B.append(0)
            if W - sumB >= truck[0]: # 만약 총 무게 - 다리위 트럭 무게가 현재 대기줄 맨 앞 트럭 무게보다 크거나 같다면
                sumB += truck[0]
                B[-1] = truck[0] # 다리에 입장
                truck.popleft() # 대기줄 맨 앞 트럭 pop

    return sec + bridge_length # 다리길이를 더하는 이유는 트럭 대기줄에서 마지막 트럭이 다리에 오르는 순간
                               # while문이 종료 되기 때문에 마지막 트럭이 다리를 건너는 초를 더해줘야한다