n = int(input())
c = 0 # 거스름돈 개수
excep = [1, 3] # X...X1, X...X3, X...X6, X...X8

if n >= 2:
  if n == 3:
    c = -1
  elif (n % 5) in excep: 
    c += (n // 5) - 1
    n %= 5
    c += (n + 5) // 2
  else:
    c += (n // 5)
    n %= 5
    c += (n // 2)
else:
  c = -1

print(c)
