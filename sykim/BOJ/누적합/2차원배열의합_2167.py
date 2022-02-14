import sys

input = sys.stdin.readline

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
memo = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        memo[i][j] = arr[i - 1][j - 1] + memo[i][j - 1] + memo[i - 1][j] - memo[i - 1][j - 1]

k = int(input())
for _ in range(k):
    i, j, x, y = map(int, input().split())
    print(memo[x][y] - memo[i - 1][y] - memo[x][j - 1] + memo[i - 1][j - 1])

# 참고 : https://ywtechit.tistory.com/102
# 참고: https://ywtechit.tistory.com/78?category=930709
# key : 여러번 사용될 정보는 구해서 저장하자



# key: 2차원을 1차원으로 흩으리는 것
####n,m = list(map(int,input().split()))
# nums = []
# for i in range(n):
#     nums.append(list(map(int,input().split())))
# select = []
# k = int(input())
# for i in range(k):
#     i,j,x,y = list(map(int,input().split()))
#     select.append([j-1,i-1,y-1,x-1])
#
# # change axis of nums
# nums = list(map(list,zip(*nums)))
#
# # sumList = []
# for idxs in select:
#     totalSum = 0
#     new_i,new_j,new_x,new_y = idxs
#     for idx_row in range(new_i, new_x+1):
#         for idx_col in range(new_j, new_y+1):
#             totalSum += nums[idx_row][idx_col]
#     print(totalSum)
#
# todo
# reverse 안하고 풀어보기.. 시간초과뜸 ㅎ

