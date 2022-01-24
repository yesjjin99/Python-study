N, M = list(map(int, input().split()))

maps = list()
for _ in range(N):
    maps.append(list(map(int, input().split())))

xy = list()
for _ in range(M):
    xy.append(list(map(int, input().split())))

# 구간합 구하기
prefix = [[0] * (N + 1)]
for x in range(1, N + 1):
    ans, p_sum, c_sum = 0, 0, 0
    ans_l = [0]
    for y in range(1, N + 1):
        p_sum = prefix[x - 1][y]
        c_sum += maps[x - 1][y - 1]
        ans = p_sum + c_sum
        ans_l.append(ans)
    prefix.append(ans_l)

ans = 0
for x1, y1, x2, y2 in xy:
    ans = prefix[x2][y2] - prefix[x1 - 1][y2] - prefix[x2][y1 - 1] + prefix[x1 - 1][y1 - 1]
    print(ans)

# sum으로 구하면 시간초과
'''
for x1, y1, x2, y2 in xy:
    ans = 0

    for i in range(x1-1, x2):
        ans += sum(maps[i][y1-1:y2])
    print(ans)
'''