t = int(input())
for i in range(t):
  arr = list(input())
  n = 0
  for j in arr:
    if j == '(':
      n += 1
    elif j == ')':
      n -= 1
    if n < 0: # ())(() - NO 와 같은 경우
      print('NO')
      break
  if n == 0:
    print('YES')
  elif n > 0:
    print('NO')


'''
stack 사용 ver.
t = int(input())
for i in range(t):
  arr = list(input())
  n = []
  for j in arr:
    if j == '(':
      n.append(j)
    elif j == ')':
      if len(n) != 0 and n[-1] == '(':
        n.pop()
      else: # ())(() - NO 와 같은 경우
        n.append(j)
        break
  if len(n) == 0:
    print('YES')
  else:
    print('NO')
'''