import sys
from collections import defaultdict
input = sys.stdin.readline

tree = defaultdict(int)
num = 0

while True:
  s = input().rstrip()
  if not s:
    break # 입력 종료
  tree[s] += 1
  num += 1

sorted = list(tree.keys())
sorted.sort()

for d in sorted:
  print(d, '%.4f' % (tree[d] / num * 100))