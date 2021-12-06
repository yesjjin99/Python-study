n = int(input())
w = list()

for _ in range(n):
    w.append(int(input()))

w = sorted(w, reverse=True)

max_w = 0
cnt_w = 0
for i in range(n):
    cnt_w += 1
    tmp_w = w[i]*cnt_w
    if max_w < tmp_w:
        max_w = tmp_w

print(max_w)