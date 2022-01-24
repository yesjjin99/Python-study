N = int(input())

maps = list()
for _ in range(N):
    maps.append(list(map(int, input().split())))

ans = [0, 0]
def func(start_i, end_i):
    s_r, s_c = start_i
    e_r, e_c = end_i
    color = maps[s_r][s_c] # 첫번째 색깔 저장
    ckt = True # True로 초기화. 모든 종이의 색이 같으면 True, 다르면 False
    for r in range(s_r, e_r+1):
        if not ckt:
            break
        for c in range(s_c, e_c+1):
            if maps[r][c] != color: # color와 다른 색 종이라면
                ckt = False # ckt를 False로 설정
                break

    if ckt: # 모든 종이가 같은 색일때
        if color == 0:
            ans[0] += 1
        else:
            ans[1] += 1
        return 0
    else: # 종이 색깔이 다를 때
        mid_r, mid_c = (s_r+e_r)//2, (s_c+e_c)//2 # 가운데를 기점으로 4군데로 나눔
        func(start_i, (mid_r, mid_c)) # 왼쪽 위
        func((start_i[0], mid_c+1), (mid_r, end_i[1])) # 오른쪽 위
        func((mid_r+1, start_i[1]), (end_i[0], mid_c)) # 왼쪽 아래
        func((mid_r+1, mid_c+1), end_i) # 오른쪽 아래

func((0, 0), (N-1, N-1))

for i in range(2):
    print(ans[i])