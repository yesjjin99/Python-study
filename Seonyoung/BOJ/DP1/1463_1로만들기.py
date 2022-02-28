N = int(input())

ans = [0] * (N + 1)

for i in range(2, N + 1):
    ans[i] = ans[i - 1] + 1

    if i % 3 == 0:
        ans[i] = min(ans[i], ans[i // 3] + 1)
    if i % 2 == 0:
        ans[i] = min(ans[i], ans[i // 2] + 1)

print(ans[N])