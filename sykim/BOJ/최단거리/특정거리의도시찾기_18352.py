import sys
from collections import defaultdict,deque

input = sys.stdin.readline

n, m, k, x = list(map(int,input().split()))
graph = [[] for _ in range(n+1)]
for _ in range(m):
    src, dst = list(map(int,input().split()))
    graph[src].append(dst)

dist = 0
q = deque()
q.append((x,dist))
visited = [False]*(n+1)
memories = defaultdict(list)
visited[x] = True

# 단방향일 때
while q:
    src,dist = q.popleft()
    for adj in graph[src]:
        if not visited[adj]:
            q.append((adj,dist+1))
            if src == adj:
                memories[0].append(adj)
            else:
                memories[dist+1].append(adj)
            visited[adj] = True

if memories[k]:
    memories[k].sort()
    for val in memories[k]:
        print(val)
else:
    print(-1)

##key: 최단거리 -> dfs말고 BFS!
