# 다시 풀어보기!

import copy

r, c = map(int, input().split())
land = []
for _ in range(r):
  land.append(list(input()))

answer = copy.deecopy(land) # 2차원 배열부터는 deecopy 써야 함
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for x in range(r):
  for y in range(c):
    if land[x][y] == '.':
      continue
    count = 0
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if nx < 0 or nx >= r or ny < 0 or ny >= c:
        count += 1
      elif land[nx][ny] == '.':
        count += 1
      
    if count >= 3:
      answer[x][y] = '.'

# 출력
startR, endR = 0, 0
startC, endC = c - 1, 0

for i in range(r):
  if 'X' in answer[i]:
    startR = i
    break

for i in range(r - 1, -1, -1):
  if 'X' in answer[i]:
    endR = i
    break

for i in range(startR, endR + 1):
  tmp = [k for k, v in enumerate(answer[i]) if v == 'X']
  if not tmp:
    continue
  startC = min(startC, tmp[0])
  endC = max(endC, tmp[-1])

for i in range(startR, endR + 1):
  for j in range(startC, endC + 1):
    print(answer[i][j], end = '')
  print()
