from collections import deque

n, k = input().split()
q = deque()
for i in range(int(n)):
  q.append(i + 1)

answer = deque()
while(q):
  q.rotate(-(int(k) - 1)) # 원형큐
  answer.append(q.popleft())

print("<", ', '.join(map(str, answer)), ">", sep='')
