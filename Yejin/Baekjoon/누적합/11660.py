import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = []
for _ in range(n):
  arr.append(list(map(int, input().split())))

# 구간합(DP)
dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
for i in range(1, n + 1):
  for j in range(1, n + 1):
    dp[i][j] = dp[i][j - 1] + dp[i - 1][j] - dp[i - 1][j - 1] + arr[i - 1][j - 1]

# 주어진 범위 내 합 구하기
for _ in range(m):
  x1, y1, x2, y2 = map(int, input().split())
  answer = dp[x2][y2] - dp[x2][y1 - 1] - dp[x1 - 1][y2] + dp[x1 - 1][y1 - 1]
  print(answer)