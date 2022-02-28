n = int(input())
tips = []
answer = 0
for _ in range(n):
  tips.append(int(input()))

tips.sort(reverse=True)
for i in range(len(tips)):
  t = tips[i] - i
  if t > 0:
    answer += t

print(answer)