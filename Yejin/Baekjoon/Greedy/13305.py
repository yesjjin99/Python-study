import sys
input = sys.stdin.readline

n = int(input())
road = list(map(int, input().split())) # n - 1
cost = list(map(int, input().split())) # n

answer = 0
m = cost[0]
for i in range(n - 1):
  # 지나온 주유소 중 가장 저렴한 가격의 주유소에서 기름 넣음
  if cost[i] < m:
    m = cost[i]
  answer += m * road[i]

print(answer)