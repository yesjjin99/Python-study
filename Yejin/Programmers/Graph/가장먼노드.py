from collections import deque

def solution(n, vertex):
    answer = 0
    far = 0
    graph = [[] * n for i in range(n + 1)]
    for i in range(len(vertex)): # 인접 행렬로
        graph[vertex[i][0]].append(vertex[i][1])
        graph[vertex[i][1]].append(vertex[i][0])
            
    def bfs(v):
        queue = deque([v])
        visited = []
        visited.append(v)
        edges = [0 for i in range(n + 1)]
        while queue:
            if len(visited) == n:
                return far, edges
            v = queue.popleft()
            for i in graph[v]: # runtime error
                if i not in visited:
                    queue.append(i)
                    visited.append(i)
                    edges[i] = edges[v] + 1
                    far = edges[i]
                    
    far, edges = bfs(1)
    for i in range(n + 1):
        if edges[i] == far:
            answer += 1
    return answer