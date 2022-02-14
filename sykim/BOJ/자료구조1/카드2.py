import sys
from collections import deque
input = sys.stdin.readline

# 1번 카드 제일 위
# N번 카드 제일 아래
# [1,2,3...N]
# [2,3,..N] -> [3,4..N,2]

N = int(input())
cards = list(range(1,N+1))
cards = deque(cards)

while len(cards)>1:
    cards.popleft()
    sec = cards.popleft()
    cards.append(sec)
print(cards.pop())