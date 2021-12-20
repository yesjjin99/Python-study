n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# 1. sort
print(' '.join(map(str, sorted(a + b))))

# 2. two-pointer
pa = 0
pb = 0
answer = []

while pa != n or pb != m:
  if pa == n:
    answer.append(b[pb]) # 맨 끝까지 간 경우(가장 마지막)
    pb += 1
  elif pb == m:
    answer.append(a[pa])
    pa += 1
  else:
    if a[pa] < b[pb]:
      answer.append(a[pa])
      pa += 1
    else:
      answer.append(b[pb])
      pb += 1

print(' '.join(map(str, answer)))
# print(*answer)