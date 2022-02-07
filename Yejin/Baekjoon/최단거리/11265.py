import sys
input = sys.stdin.readline # 시간 초과

n, m = map(int, input().split())
time = [list(map(int, input().split())) for _ in range(n)]

# 최단거리: 플로이드 워셜 알고리즘
for k in range(n): # 거치는 노드
  for i in range(n): # 시작점
    for j in range(n): # 끝점
      if time[i][j] > time[i][k] + time[k][j]:
        time[i][j] = time[i][k] + time[k][j]

for _ in range(m):
  a, b, c = map(int, input().split())
  if time[a-1][b-1] <= c: # 시간 내
    print('Enjoy other party')
  else:
    print('Stay here')