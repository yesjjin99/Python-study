from collections import deque

n = int(input())
edge_num = int(input())

graph = dict()
for i in range(n+1):
    graph[i] = set()

edge_list = list()

for _ in range(edge_num):
    edge_list.append(list(map(int, input().split())))

for nodes in edge_list:
    graph[nodes[0]].add(nodes[1])
    graph[nodes[1]].add(nodes[0])

def dfs(graph, start_node):
    visited = []
    stack = deque([start_node])

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            stack.extend(list(graph[node]))
    return visited

visit = dfs(graph, 1)
print(len(visit)-1)
