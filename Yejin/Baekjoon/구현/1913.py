n = int(input())
t = int(input())
table = [[0] * n for _ in range(n)]
# 위쪽, 오른쪽, 아래쪽, 왼쪽
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

x, y = n//2, n//2
cnt, m, num = 1, 0, 1
table[x][y] = num
while True:
    for _ in range(cnt):
        x += dx[m]
        y += dy[m]
        num += 1
        table[x][y] = num

        if num == n**2:
            break

    if num == n**2:
        break

    m = (m + 1) % 4
    if m == 0 or m == 2:
        cnt += 1 

for i in table:
    print(*i)
for i in range(n):
    for j in range(n):
        if table[i][j] == t:
            print(i + 1, j + 1)
            