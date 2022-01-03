def dfs(graph, infected, v):
  infected.append(v)
  for i in graph[v]:
    if i not in infected:
      dfs(graph, infected, i)

c = int(input())
e = int(input())
graph = [[] for _ in range(c + 1)]
infected = []
for _ in range(e):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)
for i in range(1, c + 1):
  graph[i].sort()

dfs(graph, infected, 1)
print(len(infected) - 1) # 1번 컴퓨터 제외한 수
