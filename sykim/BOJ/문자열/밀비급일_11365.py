import sys

input = sys.stdin.readline
saveSentecnes = []
while True:
    a = input().rstrip()
    if a != 'END':
        saveSentecnes.append(a)
    else:
        break
for l in saveSentecnes:
    print(l[::-1])

# 문자열 거꾸로 하기는 [::-1]