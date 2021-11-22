def solution(m, n, puddles):
    answer = 0
    path = list()
    for r in range(n):
        tmp = [0] * m
        path.append(tmp)

    path[0][0] = 1
    for r in range(n):
        for c in range(m):
            if (r, c) == (0, 0):
                continue
            if [c + 1, r + 1] in puddles:
                path[r][c] = 0
                continue

            left, down = c - 1, r - 1
            if left < 0:
                path[r][c] = path[down][c]
            elif down < 0:
                path[r][c] = path[r][left]
            else:
                path[r][c] = path[r][left] + path[down][c]
    answer = (path[n - 1][m - 1] % 1000000007)
    return answer