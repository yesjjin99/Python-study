N, M = list(map(int, input().split()))

visited = list()
def dfs():
    if len(visited) == M:
        print(' '.join(map(str, visited)))
        return

    for i in range(1, N+1):
        if i not in visited:
            visited.append(i)
            dfs()
            visited.pop()

dfs()
