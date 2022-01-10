l, r = input().split()
word = input()
answer = 0

keyL = [['q', 'w', 'e', 'r', 't'], ['a', 's', 'd', 'f', 'g'], ['z', 'x', 'c', 'v']]
keyR = [['y', 'u', 'i', 'o', 'p'], ['h', 'j', 'k', 'l'], ['b', 'n', 'm']]

key = dict()
for i, data in enumerate(keyL):
  for j, s in enumerate(data):
    key[s] = ['L', i, j] # left, 좌표

for i, data in enumerate(keyR):
  for j, s in enumerate(data):
    if i == 0 or i == 1:
      key[s] = ['R', i, j + 5]
    elif i == 2:
      key[s] = ['R', i, j + 4]

lx, ly = key[l][1], key[l][2]
rx, ry = key[r][1], key[r][2]

for s in word:
  x, y = key[s][1], key[s][2]
  if key[s][0] == 'L':
    answer += abs(x - lx) + abs(y - ly) + 1
    lx, ly = x, y
  elif key[s][0] == 'R':
    answer += abs(x - rx) + abs(y - ry) + 1
    rx, ry = x, y

print(answer)
