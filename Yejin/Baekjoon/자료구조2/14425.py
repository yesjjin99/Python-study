n, m = input().split()
s, arr = [], []
for i in range(int(n)):
  s.append(input())
for i in range(int(m)):
  arr.append(input())

c = 0
for a in arr:
  if a in s:
    c += 1
print(c)
