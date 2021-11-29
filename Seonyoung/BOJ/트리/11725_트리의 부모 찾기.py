from collections import deque

n = int(input())
graph = {new_list: [] for new_list in range(1, n + 1)}
for _ in range(n - 1):
    a, b = map(int, input().split())

    graph[a].append(b)
    graph[b].append(a)


def bfs(n, start):
    n_visit = [False] * (n + 1)
    p_list = [0] * (n + 1)
    queue = deque([start])

    while len(queue):
        n = queue.pop()
        n_visit[n] = True

        for c in graph[n]:
            if n_visit[c] == False:  # True(이미 방문한 노드)의 경우 n의 부모임
                p_list[c] = n
                queue.append(c)

    return p_list


p_list = bfs(n, 1)[2:]
for i in p_list:
    print(i)