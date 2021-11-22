from collections import deque

def bfs(n, computers, x, y):
    visited = [False] * n
    
    queue = deque()
    queue.append((x, y))
    
    while queue:
        x, y = queue.popleft()
        visited[y] = True
        for j in range(n):
            if computers[y][j] == 1:
                if not visited[j]:
                    queue.append((y, j))
                    visited[j] = True
                
                computers[y][j] = 0

def solution(n, computers):
    answer = 0
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1:
                bfs(n, computers, i, j)
                answer += 1
    return answer
    