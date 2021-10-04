from collections import deque, defaultdict

def bfs(graph, start, visited, distance):
    queue = deque([[start, 0]])
    visited[start] = True

    while queue:
        node, depth = queue.popleft()
        distance[node] = depth

        for i in graph[node]:
            if not visited[i]:
                queue.append([i, depth + 1])
                visited[i] = True
        depth += 1

    return distance.count(max(distance))

def solution(n, edge):
    # 그래프 초기화
    graph = defaultdict(list)
    for e1, e2 in edge:
        graph[e1].append(e2)
        graph[e2].append(e1)

    visited = [False] * (n + 1)
    distance = [0] * (n + 1)  # node 1번과의 거리를 저장

    d = bfs(graph, 1, visited, distance)
    return d