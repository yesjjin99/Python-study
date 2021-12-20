import sys
input = sys.stdin.readline

n, x = map(int, input().split())
visits = list(map(int, input().split()))

if max(visits) == 0:
  print('SAD')
else:
  # two-pointer, 슬라이딩 윈도우
  value = sum(visits[:x])
  total, count = value, 1
  for end in range(x, n):
    value += visits[end]
    value -= visits[end-x]
    if value > total:
      total = value
      count = 1
    elif value == total:
      count += 1
  
  print(total)
  print(count)
