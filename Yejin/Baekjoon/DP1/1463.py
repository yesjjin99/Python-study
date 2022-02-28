n = int(input())
dp = [0] * (n + 1) # memoization

for i in range(2, n + 1):
  dp[i] = dp[i-1] + 1 # 1을 빼는 경우
  if i % 3 == 0:
    dp[i] = min(dp[i], dp[i//3] + 1) # 3으로 나눈 경우이므로 횟수 추가해줘야 함 -> +1
  if i % 2 == 0:
    dp[i] = min(dp[i], dp[i//2] + 1)

print(dp[n])