# 아스키 코드 이용
n, b = input().split()
answer, c = 0, 0
for i in n[::-1]: # 거꾸로 
  num = int(i) if i.isdigit() else ord(i) - 55 # ord('A') = 65
  answer += num * (int(b) ** c)
  c += 1

print(answer)
