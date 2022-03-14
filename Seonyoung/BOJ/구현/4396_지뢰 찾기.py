'''
1. 게임 맵에서 좌표를 하나씩 확인하면서 주위 지뢰들 개수를 업데이트
    (만약 지뢰가 열렸다면, 지뢰가 열렸음을 표시)
2. 지뢰가 열렸다면, 모든 지뢰 좌표의 내용을 '*'로 업데이트 해줌
'''

n = int(input())

bomb = list()  # 지뢰 지도
bomb_loc = list()  # 지뢰 좌표
for r, _ in enumerate(range(n)):
    tmp = list(map(str, input().rstrip()))
    for c, i in enumerate(tmp):
        if i == '*':
            bomb_loc.append([r, c])
    bomb.append(tmp)

board = list()  # 게임 맵
for _ in range(n):
    tmp = list(map(str, input().rstrip()))
    board.append(tmp)

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]
click_bomb = False
ans = list()
for x in range(n):
    tmp = list()
    for y in range(n):
        cnt = 0
        if board[x][y] == 'x':  # 클릭한 상태
            if bomb[x][y] == '*':  # 지뢰가 열렸음
                click_bomb = True

            for i in range(8):
                X = x + dx[i]
                Y = y + dy[i]
                if X < 0 or X >= n or Y < 0 or Y >= n:
                    continue
                if bomb[X][Y] == '*':  # 지뢰 존재
                    cnt += 1
            tmp.append(cnt)
        else:  # 클릭 안한 상태
            tmp.append('.')
    ans.append(tmp)

if click_bomb:
    for r, c in bomb_loc:
        ans[r][c] = '*'

for l in ans:
    print(''.join(map(str, l)))