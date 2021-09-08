INF = 1e10
def floyd(dist, n):
    # i->j로 가는 최단거리를 저장하려고 하는거임
    # k라는 경유지를 두고 i에서 j로 갈때 i->k->j가 빠른지 현재의 i->j가 빠른지 비교
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][k] + dist[k][j], dist[i][j])

def solution(n, s, a, b, fares):
    # dist -> x에서 y로 가는 운임 나타내는 2차원 요금지도
    dist = [[INF for _ in range(n)] for _ in range(n)]

    # 나 자신 -> 나 자신인 경우 0으로 설정
    for i in range(n):
        dist[i][i] = 0

    # fares로 받은 운임 적용해주기
    for info in fares:
        # 우린 인덱스를 0부터 쓰니깐 -1해주자
        dist[info[0] - 1][info[1] - 1] = info[2]
        # 양방향으로 적용
        dist[info[1] - 1][info[0] - 1] = info[2]

    # 플로이드워셜 알고리즘 이용해서 2차원 요금지도 완성
    floyd(dist, n)
    # for i in range(n):
    #     print(*dist[i])

    # s, a, b 역시 -1 해줘야 인덱스가 맞음
    s -= 1
    a -= 1
    b -= 1
    answer = INF
    # k라는 경유지까지 합승하고 그곳에서 갈라지는 경우의 수 모두 비교
    # k에는 출발지도 포함되므로 (dist[s][s]도 있다는 뜻)
    # 합승안하는 경우도 체크할 수 있음
    for k in range(n):
        answer = min(answer, dist[s][k] + dist[k][a] + dist[k][b])

    return answer