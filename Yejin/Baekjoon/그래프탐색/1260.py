from collections import deque

def dfs(graph, visited, n, v):
  visited[v] = True
  print(v, end = ' ')
  for g in graph[v]:
    if not visited[g]: # False
      dfs(graph, visited, n, g)

def bfs(graph, visited, v):
  queue = deque([v])
  visited[v] = True
  while queue:
    v = queue.popleft()
    print(v, end = ' ')
    for g in graph[v]:
      if not visited[g]: # False
        queue.append(g)
        visited[g] = True

n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append(b) # 양방향
  graph[b].append(a)
for i in range(1, n + 1):
  graph[i].sort()

dfs(graph, visited, n, v)
visited = [False] * (n + 1)
print()
bfs(graph, visited, v)
