def factorial(a):
  f = 1
  for i in range(a):
    f *= (i + 1)
  return f

t = int(input())
for _ in range(t):
  n, m = map(int, input().split())
  print(factorial(m) // (factorial(m - n) * factorial(n)))
  