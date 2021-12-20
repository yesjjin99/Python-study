n, k = map(int, input().split())
items = [list(map(int, input().split())) for _ in range(n)] # [w, v]

dp = [[0 for _ in range(k + 1)] for _ in range(n + 1)]
for i in range(1, n + 1): # 물품
  for j in range(1, k + 1): # 무게
    if j >= items[i-1][0]:
      dp[i][j] = max(dp[i-1][j], dp[i-1][j-items[i-1][0]] + items[i-1][1])
    else:
      dp[i][j] = dp[i-1][j]

print(dp[n][k])
