import sys

n, m = input().split()
poket_str, poket_int = {}, {} # dict
for i in range(int(n)):
  s = input()
  poket_str[s] = i + 1
  poket_int[i + 1] = s

for _ in range(int(m)):
  p = sys.stdin.readline().rstrip() # 시간초과
  if p.isdigit():
    print(poket_int[int(p)])
  else:
    print(poket_str[p])
