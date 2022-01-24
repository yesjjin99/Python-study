import copy

N = int(input())

maps = list()
for _ in range(N):
    maps.append(list(map(int, input().split())))

# (r, c)칸으로부터 2x2 풀링을 하는 함수
def slice_list(r, c, maps):
    tmp = list()
    for i in range(r, r + 2):
        for j in range(c, c + 2):
            tmp.append(maps[i][j])
    ans = sorted(tmp, reverse=True)
    return ans[1]


while len(maps) > 1:
    tmp_maps = list()

    for r in range(0, len(maps) - 1, 2):
        num = list()
        for c in range(0, len(maps) - 1, 2):
            small_map = slice_list(r, c, maps)
            num.append(small_map)
        tmp_maps.append(num)
    maps = copy.deepcopy(tmp_maps)

print(maps[0][0])