n, m = map(int, input().split())
avoid = [[] for _ in range(n + 1)]
answer = 0
for _ in range(m):
  a, b = map(int, input().split())
  avoid[a].append(b)
  avoid[b].append(a)

for i in range(1, n + 1):
  for j in range(i + 1, n + 1):
    if j in avoid[i]:
      continue
    for k in range(j + 1, n + 1):
      if k in avoid[j] or k in avoid[i]:
        continue
      else:
        answer += 1

print(answer)
