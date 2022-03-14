N, M = map(int, input().split())

graph = dict()
for _ in range(M):
    child, parent = map(int, input().split())
    if parent not in graph.keys():
        graph[parent] = [child]
    else:
        graph[parent].append(child)


def dfs(root):
    stack = [root]
    visit = [False] * (N + 1)
    visit[root] = True

    cnt = 0
    while stack:
        node = stack.pop()

        if node not in graph.keys():
            continue

        for i in graph[node]:
            if not visit[i]:
                cnt += 1 # 자식 노드 개수 세기
                stack.append(i)
                visit[i] = True

    return cnt


max_v = 0
ans = list()
for i in range(1, N + 1):
    cnt = dfs(i)
    if max_v < cnt:
        ans = [i]
        max_v = cnt
    elif max_v == cnt:
        ans.append(i)

ans.sort()
print(' '.join(map(str, ans)))