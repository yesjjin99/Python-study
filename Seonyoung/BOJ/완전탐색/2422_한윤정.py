n, m = list(map(int, input().split()))

# 1. 불가능한 조합을 ice_comb에 저장
ice_comb = {i: [] for i in range(1, n + 1)}
for _ in range(m):
    comb = list(map(int, input().split()))
    ice_comb[comb[0]].append(comb[1])
    ice_comb[comb[1]].append(comb[0])

ans = 0
# 2. (i, j, k) 조합 생성
for i in range(1, n - 1):
    for j in range(i + 1, n):
        # 2-1. (i, j) 조합 검사
        if j in ice_comb[i]:
            continue

        for k in range(j + 1, n + 1):
            # 2-2. (i, k), (j, k) 조합 검사
            if k in ice_comb[i] or k in ice_comb[j]:
                continue
            ans += 1

print(ans)
