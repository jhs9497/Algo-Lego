from collections import deque

def solution(n, edge):
    
    # 연결 노드를 저장해 줄 이차원 리스트
    nodes = [[] for _ in range(n+1)]
    
    for x, y in edge:
        # x번째 인덱스에 y append
        nodes[x].append(y)
        # y번째 인덱스에 x append
        nodes[y].append(x)
        
    def bfs(now):
        # 바로 직전에 지나온 위치를 저장해줄 리스트
        roads = [-1]*(n+1)
        # 첫 번째 위치는 0으로 초기화
        roads[1] = 0
        # 지나쳐온 길의 수를 저장해 줄 리스트
        ans = [0]*(n+1)
        # q는 현재 위치에서 갈 수 있는 다음 위치들을 저장해줄 리스트
        q = deque()
        # 첫번째 위치 append
        q.append(now)
        # q가 남아있는 동안
        while q:
            # 가장 앞에 거를 빼서 현재 위치로 업데이트
            now = q.popleft()
            # 현재 위치에서 이동 가능한 좌표 중
            for x in nodes[now]:
                # 이미 가본 기록이 있는 곳은 실행 X
                if roads[x] != -1:
                    continue
                # 그렇지 않다면 q에 append해주고
                q.append(x)
                # 이전 위치에서 + 1을 한 값으로 지나쳐온 길의 수 업데이트
                ans[x] = ans[now] + 1
                # 직전 위치를 road에 저장
                roads[x] = now
        
        return ans

    lst = bfs(1)
    max_num = max(lst)
    
    return lst.count(max_num)