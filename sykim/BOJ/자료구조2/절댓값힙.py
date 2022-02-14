import sys
import heapq
input = sys.stdin.readline
# key : 다 받고나서 처리하자.
N = int(input())
nums = []
result = []
for _ in range(N):
    idx = int(input())
    # nums.append(idx)
    if idx ==0:

        if not nums:
            result.append(0)
        else:
            abs_val, min_val = heapq.heappop(nums)
            result.append(min_val)

            # while (abs_val,min_val) in nums:
            #     heapq.heappop(nums)
            #     print('dd')
    else:
        heapq.heappush(nums,(abs(idx),idx))
print('--')

for v in result:
    print(v)

