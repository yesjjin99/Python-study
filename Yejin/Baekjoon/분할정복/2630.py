n = int(input())
white, blue = 0, 0
arr = []
for _ in range(n): # 0 하얀색, 1 파란색
  arr.append(list(map(int, input().split())))

def slice(x, y, n):
  global white, blue
  color = arr[x][y] # 0 or 1
  for i in range(x, x + n):
    for j in range(y, y + n):
      # 4분면으로 분할 후 계산
      if color != arr[i][j]: # 모든 구간이 같은 색이 아닌 경우
        slice(x, y, n // 2)
        slice(x, y + n // 2, n // 2)
        slice(x + n // 2, y, n // 2)
        slice(x + n // 2, y + n // 2, n // 2)
        return
  if color == 0:
    white += 1
  else:
    blue += 1

slice(0, 0, n)
print(white)
print(blue)