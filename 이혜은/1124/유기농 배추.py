for tc in range(int(input())):
  M, N, K = map(int, input().split())
  road = [[0]*M for _ in range(N)]

  for k in range(K):
    X, Y = map(int, input().split())
    road[Y][X] = 1

  ans = 0
  
  dr = [-1, 1, 0, 0]
  dc = [0, 0, -1, 1]

  def dfs(r, c):
    
    s = []
    s.append((r, c))
    while s:
      r, c = s.pop()
      road[r][c] = 0
      for di in range(4):
        nr = r + dr[di]
        nc = c + dc[di]
        if nr >= N or nr < 0 or nc >= M or nc < 0:
          continue
        if road[nr][nc] == 1:
          s.append((nr, nc))

  for i in range(N):
    for j in range(M):
      if road[i][j] == 1:
        dfs(i, j)
        ans += 1
    
  print(ans)