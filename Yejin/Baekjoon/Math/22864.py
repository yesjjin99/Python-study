a, b, c, m = map(int, input().split())
t, w = 0, 0 # 피로도, 일 count
for _ in range(24): # 종료조건 : 하루는 24시간
  if a > m:
    break
  if t + a > m: # rest
    t -= c
    if t < 0:
      break
  else:
    t += a
    w += b

print(w)
