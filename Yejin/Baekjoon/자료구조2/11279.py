import heapq
import sys

heap = []
n = int(input())
for _ in range(n):
  x = int(sys.stdin.readline().rstrip())
  if x == 0:
    if len(heap) == 0:
      print(0)
    else:
      print(heapq.heappop(heap)[1]) # (-x, x) 에서 두 번째 원소인 x print
  else:
    heapq.heappush(heap, (-x, x))
    