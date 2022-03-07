'''
0~N까지의 정수 K개를 더해서 합이 N이 되는 경우의 수를 구해야할 때
ex) N = 6, K = 4
6 = 0 + (합이 6인 3개의 정수)
    1 + (합이 5인 3개의 정수)
    ...
    6 + (합이 0인 3개의 정수)

k개의 정수로 n을 만들 수 있는 경우의 수를 dp[k][n]이라고 하면
dp[k][n] = dp[k-1][0] + dp[k-1][1] + ... + dp[k-1][n]
'''

N, K = map(int, input().split())

maps = [[0] * (N + 1) for _ in range(K + 1)]

# n을 1개의 정수로 나타내는 방법은 자기자신으로만 나타낼 수 있음
for c in range(N + 1):
    maps[1][c] = 1

for k in range(2, K + 1):
    for n in range(N + 1):
        for i in range(n + 1):
            maps[k][n] += maps[k - 1][i]

print(maps[K][N] % 1000000000)