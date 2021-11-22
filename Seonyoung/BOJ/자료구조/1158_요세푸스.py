n, k = map(int, input().split())
circle = []
for i in range(1, n+1):
    circle.append(i)

answer = []
target_idx = 0
len_circle = n
while len_circle:
    target_idx = (target_idx+(k-1)) % len_circle
    answer.append(circle[target_idx])
    del circle[target_idx]
    len_circle -= 1

answer_list = ', '.join(map(str, answer))

print(f'<{answer_list}>')