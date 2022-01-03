n = int(input())

people = dict()
for i in range(1, n ** 2 + 1):
    info = list(map(int, input().split()))
    people[info[0]] = info[1:]

seats = list()
for i in range(n):
    tmp = [0] * n
    seats.append(tmp)

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
for i in people.keys():
    candidate = dict()
    saved_liked, saved_empty, saved_loc = 0, 0, (-1, -1)
    for r in range(n):
        for c in range(n):
            if seats[r][c] != 0:  # 빈자리가 아닐 경우
                continue

            liked, empty, loc = 0, 0, (r, c)
            for k in range(4):  # 인접 자리 검사
                x = r + dx[k]
                y = c + dy[k]
                if x < 0 or x >= n or y < 0 or y >= n:
                    continue

                if seats[x][y] == 0:  # 조건 2. 빈 자리일 경우
                    empty += 1
                elif seats[x][y] in people[i]:  # 조건 1. 빈 자리가 아닐 경우, 좋아하는 사람인지
                    liked += 1

            if saved_liked < liked:
                saved_liked, saved_empty, saved_loc = liked, empty, (r, c)
            elif saved_liked == liked:  # 조건 1 불충분
                if saved_empty < empty:
                    saved_liked, saved_empty, saved_loc = liked, empty, (r, c)
                elif saved_empty == empty:  # 조건 2 불충분
                    if saved_loc == (-1, -1):
                        saved_liked, saved_empty, saved_loc = liked, empty, (r, c)
                    elif saved_loc[0] > loc[0]:
                        saved_liked, saved_empty, saved_loc = liked, empty, (r, c)
                    elif saved_loc[0] == loc[0]:  # 조건 3-(1) 불충분
                        if saved_loc[1] > loc[1]:
                            saved_liked, saved_empty, saved_loc = liked, empty, (r, c)
    seats[saved_loc[0]][saved_loc[1]] = i

answer = 0
for r in range(n):
    for c in range(n):
        liked = 0
        person_idx = seats[r][c]
        for k in range(4):  # 인접 자리 검사
            x = r + dx[k]
            y = c + dy[k]
            if x < 0 or x >= n or y < 0 or y >= n:
                continue

            if seats[x][y] in people[person_idx]:
                liked += 1
        if liked == 1:
            answer += 1
        elif liked == 2:
            answer += 10
        elif liked == 3:
            answer += 100
        elif liked == 4:
            answer += 1000

print(answer)
