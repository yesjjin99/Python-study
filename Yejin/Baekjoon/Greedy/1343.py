board = input().split('.')
answer = []

for b in board:
  l = len(b)
  if l % 2 == 0:
    if l % 4 == 0:
      answer.append('A' * l)
      answer.append('.')
    else:
      answer.append('A' * (l - 2) + 'BB')
      answer.append('.')
  else:
    answer.clear()
    answer.append(-1)
    answer.append('.')
    break

answer.pop() # 마지막에 추가된 '.' 하나 빼줘야 함
print(answer[0]) if answer[0] == -1 else print("".join(answer))
