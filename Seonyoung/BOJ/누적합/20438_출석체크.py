N, K, Q, M = list(map(int, input().split()))

sleep = list(map(int, input().split()))
attend_code = list(map(int, input().split()))

section = list()
for _ in range(M):
    section.append(list(map(int, input().split())))

sleep_ckt = dict()  # 자고있으면 True, 아니면 False
for i in range(3, N + 3):
    sleep_ckt[i] = False

for i in sleep:  # 자고있는 학생을 True로 바꿔줌
    sleep_ckt[i] = True

attend_ckt = [1] * (N + 3)  # 1: 출석 X, 0: 출석 O
for s in attend_code:
    if sleep_ckt[s]:  # 자고있으면 코드 못 보냄
        continue

    i = 1
    x = s
    while x <= N + 2:
        if not sleep_ckt[x]:
            attend_ckt[x] = 0
        i += 1
        x = i * s

prefix = [0, 0, 0]
tmp = 0
for i in attend_ckt[3:]:
    tmp += i
    prefix.append(tmp)

for s, e in section:
    ans = prefix[e] - prefix[s - 1]
    print(ans)