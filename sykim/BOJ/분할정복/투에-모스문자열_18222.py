# key: 문제를 어떻게 나눌 것인가
# Q1. 어떻게 sub문제로 나눌 수 있지?
# A1. 투에-모스 점화식..;
# https://sojeong-lululala.tistory.com/66?category=1011365
import sys
input = sys.stdin.readline

k = int(input())


def find(x):
    if x == 0:
        return 0

    elif x == 1:
        return 1

    elif x % 2 == 0:
        return find(x // 2)

    else:
        return 1 - find(x // 2)


print(find(k - 1))
