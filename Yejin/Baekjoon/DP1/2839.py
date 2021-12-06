# DP -> 반복문 + 점화식!

n = int(input())
c = 0 # 봉지의 개수

while True:
  if n % 5 == 0:
    c += (n // 5)
    break
  n -= 3
  c += 1
  if n < 0:
    c = -1
    break

print(c)
