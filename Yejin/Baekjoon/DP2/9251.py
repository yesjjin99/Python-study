s1 = input()
s2 = input()
dp = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]

for i in range(1, len(s1) + 1):
  for j in range(1, len(s2) + 1):
    if s2[j-1] == s1[i-1]:
      dp[i][j] = dp[i-1][j-1] + 1 # s1, s2에 각각 문자열을 더해주기 전 개수 + 1
    else:
      dp[i][j] = max(dp[i][j-1], dp[i-1][j])

print(dp[-1][-1])