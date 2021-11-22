import heapq
import sys

input = sys.stdin.readline

n = int(input())
command = []
for _ in range(n):
    command.append(int(input()))

heap = []
heapq.heapify(heap)
for i in command:
    if i == 0 and len(heap) == 0:
        print(0)
    elif i == 0:
        print(abs(heapq.heappop(heap)))
    else:
        heapq.heappush(heap, -i)