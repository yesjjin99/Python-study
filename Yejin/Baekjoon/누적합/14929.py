import sys
input = sys.stdin.readline

n = int(input())
x = list(map(int, input().split()))
num, answer = [x[-1]], 0

# 부분합
for i in range(1, n - 1):
  # num = [xn, ... , xn+...+x3, xn+...+x2]
  num.append(num[i - 1] + x[-(i + 1)])

num.reverse()
for i in range(n - 1):
  # x1(x2+...+xn) + ... + xn-1(xn)
  answer += x[i] * num[i]

print(answer)