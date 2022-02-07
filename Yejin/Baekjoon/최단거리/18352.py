import heapq
import sys
input = sys.stdin.readline # 시간 초과
INF = int(1e9)

n, m, k, x = map(int, input().split())
path = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
  a, b = map(int, input().split())
  path[a].append(b)

def dijkstra(start):
  q = []
  heapq.heappush(q, (0, start)) # (최단거리, 현재 노드)
  distance[start] = 0

  while q:
    dist, now = heapq.heappop(q)

    if distance[now] < dist:
      continue

    for p in path[now]:
      cost = dist + 1
      if cost < distance[p]:
        distance[p] = cost # 최단 거리 갱신
        heapq.heappush(q, (cost, p))

dijkstra(x)

answer = []
for i in range(1, n + 1):
  if distance[i] == k:
    answer.append(i)

if len(answer) == 0:
  print(-1)
else:
  for i in answer:
    print(i)