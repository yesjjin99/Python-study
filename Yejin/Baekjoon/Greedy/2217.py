n = int(input())
w, answer = [], []
for _ in range(n):
  weight = int(input())
  w.append(weight)

w.sort(reverse = True)
for i in range(n):
  answer.append((i + 1) * w[i]) # w(answer)/k <= w[i] 

print(max(answer))
