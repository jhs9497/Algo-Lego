def find(parent, x):
    # 만일 자기 자신이라면 현재 출발 지점은 자신
    if parent[x] == x:
        return x
    # 아니라면 연결된 노드 존재 -> 연결된 지점의 최상단 찾기
    parent[x] = find(parent, parent[x])
    
    return parent[x]

def union(parent, a, b):
    # root는 각각의 최상위 부모
    rootA = find(parent, a)
    rootB = find(parent, b)

    # 더 작은 쪽으로 맞춰줌
    if rootA < rootB:
        parent[rootB] = rootA
    else:
        parent[rootA] = rootB

def solution(n, costs):
    answer = 0
    # 출발 지점을 저장할 parent
    parent = [0]*n
    
    # 우선 자기 자신으로 parent를 초기화
    for i in range(n):
        parent[i] = i
    
    # 비용에 따라 정렬
    costs = sorted(costs, key = lambda x : x[2])
    
    for cost in costs:
        # s와 e는 연결 포인트, cnt는 비용
        s, e, cnt = cost
        # 다를 때만(같다면 cycle 생성)
        if find(parent, s) != find(parent, e):
            # 부모 통일
            union(parent, s, e)
            answer += cnt
    
    return answer