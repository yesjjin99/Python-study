h1, m1, s1 = list(map(int, input().rstrip().split(':')))
h2, m2, s2 = list(map(int, input().rstrip().split(':')))

t1 = h1*3600 + m1*60 + s1
t2 = h2*3600 + m2*60 + s2

ans = 0

if t1 >= t2:
    ans = t2 - t1 + 24*3600 # t1 > t2일 때, t2 - t1가 마이너스이므로, 24*3600초를 더해주면 됨
else:
    ans = t2 - t1

h3 = ans // 3600
m3 = (ans%3600) // 60
s3 = (ans%3600) % 60

print('%02d:%02d:%02d' % (h3, m3, s3))