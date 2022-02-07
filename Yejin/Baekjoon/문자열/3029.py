begin = list(map(int, input().split(':')))
end = list(map(int, input().split(':')))
answer = []

s = begin[0] * 60 * 60 + begin[1] * 60 + begin[2]
e = end[0] * 60 * 60 + end[1] * 60 + end[2]

a = e - s if e > s else e - s + 24 * 60 * 60

answer.append(str(a // 60 // 60).zfill(2))
a %= 60 * 60
answer.append(str(a // 60).zfill(2))
answer.append(str(a % 60).zfill(2))

print(answer[0], answer[1], answer[2], sep = ':')