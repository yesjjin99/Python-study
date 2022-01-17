N = int(input())

# 1부터 x까지의 합
def sumN(x):
    return int(x * (x + 1) / 2)

start = 1
end = N - 1
mid = int((start + end) / 2)


ans = 0
while (start <= end):
    mid = int((start + end) / 2)

    if sumN(mid) <= N:
        ans = mid
        start = mid + 1
    elif sumN(mid) > N:
        end = mid - 1

print(ans)


# 다른 풀이 (이분탐색 사용 X)
'''
N = int(input())
n = 1
while n * (n + 1) / 2 <= N:
    n += 1
print(n - 1)
'''