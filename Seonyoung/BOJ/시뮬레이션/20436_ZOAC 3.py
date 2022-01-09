l_h, r_h = list(input().split())
word = input()

# 1. 알파벳마다 손방향(왼쪽, 오른쪽)/위치 지정
l_w = [['q', 'w', 'e', 'r', 't'],
       ['a', 's', 'd', 'f', 'g'],
       ['z', 'x', 'c', 'v']]

r_w = [['y', 'u', 'i', 'o', 'p'],
       ['h', 'j', 'k', 'l'],
       ['b', 'n', 'm']]

word_dict = dict()
for r, words in enumerate(l_w):
    for c, w in enumerate(words):
        word_dict[w] = ['l', [r, c]]

for r, words in enumerate(r_w):
    for c, w in enumerate(words):
        # 모음은 자음 다음에 오게 되어서 column index를 보정해줌
        if r == 0 or r == 1:
            c += 5
        elif r == 2:
            c += 4
        word_dict[w] = ['r', [r, c]]

# 2. 현재 왼쪽, 오른쪽 손 위치 지정
l_roc = word_dict[l_h][1]
r_roc = word_dict[r_h][1]

# 3. 이동거리 계산
ans = 0
for w in word:
    ckt, roc = word_dict[w]

    if ckt == 'l':
        d_r = abs(l_roc[0] - roc[0])
        d_c = abs(l_roc[1] - roc[1])
        l_roc = roc
    else:
        d_r = abs(r_roc[0] - roc[0])
        d_c = abs(r_roc[1] - roc[1])
        r_roc = roc

    ans += (d_r + d_c + 1)
print(ans)