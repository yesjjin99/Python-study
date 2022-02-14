import sys
import math

input = sys.stdin.readline
n = int(input())
# print(math.ceil(math.sqrt(n)))
start = 0
end = n

# 등호 주의
while True:
    # // 는 내림 연산
    mid = (start+end) //2
    if end < start:
        break

    if mid**2 < n:
        start = mid +1

    else:
        end = mid -1

print(end+1)

## key: 제곱근-> 제곱으로
# 주의: 등호 위치 + end+1로 리턴해주는 것