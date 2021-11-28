# 노드 순회하며 탐색 -> DFS/BFS
# DFS/BFS 어느 문제에서 쓸지 판단하는 연습!
import sys
sys.setrecursionlimit(10**9)
# 런타임 에러 -> 재귀 함수의 최대 깊이 늘려줘야 함 (기본적으로 1000레벨까지)

def dfs(node, tree, parent):
  for i in tree[node]:
    if parent[i] == 0:
      parent[i] = node
      dfs(i, tree, parent)

n = int(input())
tree = [[] for _ in range(n + 1)]
parent = [0 for _ in range(n + 1)]

for _ in range(n - 1):
  a, b = map(int, sys.stdin.readline().split())
  tree[a].append(b)
  tree[b].append(a)

dfs(1, tree, parent)
for i in range(2, n + 1):
  print(parent[i])
