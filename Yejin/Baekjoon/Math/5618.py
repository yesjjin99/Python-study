# Python3로 하면 시간 초과 -> PyPy3로 하면 성공
def gcd(a, b): # 최대공약수
  if a == 0: # a가 0이 될 때까지 반복
    return b
  return gcd(b % a, a)

n = int(input())
nums = list(map(int, input().split()))
g = gcd(nums[0], nums[1]) if n == 2 else gcd(nums[0], gcd(nums[1], nums[2]))
# n은 2 또는 3

for i in range(1, (g // 2) + 1): # 최대공약수의 반만큼 검사
  if g % i == 0:
    print(i)
print(g)
