from collections import deque

N = int(input())

graph = list()
ans = list()
for _ in range(N):
    tmp = list(map(int, input().split()))
    graph.append(tmp)
    ans.append(tmp.copy())


def bfs(s):
    queue = deque([s])
    visited = [False] * N

    while queue:
        node = queue.popleft()

        for i, v in enumerate(graph[node]):
            if v and not visited[i]:
                visited[i] = True
                ans[s][i] = 1
                queue.append(i)

for r in range(N):
    for c in range(N):
        if ans[r][c] == 0:
            bfs(r, c)

for k in ans:
    tmp = ' '.join(map(str, k))
    print(tmp)

'''
#입력
N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))


#플로이드-워셜 알고리즘
for k in range(N): #경로 for문이 가장 상위 단계여야 누락되지 않는다
    for i in range(N):
        for j in range(N): 
            if graph[i][j] == 1 or (graph[i][k] == 1 and graph[k][j] == 1):
                graph[i][j] = 1


#출력
for row in graph:
    for col in row:
        print(col, end = " ")
    print()
'''