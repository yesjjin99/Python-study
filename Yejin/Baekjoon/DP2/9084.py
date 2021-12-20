t = int(input())
for _ in range(t):
  n = int(input())
  coins = list(map(int, input().split()))
  m = int(input())
  
  # memorization (DP)
  dp = [0 for _ in range(m + 1)]
  dp[0] = 1
  for coin in coins:
    for i in range(1, m + 1):
      if i >= coin:
        dp[i] += dp[i-coin]
  print(dp[m])
