import sys
input = sys.stdin.readline

n= int(input())
# 1*(-2) + 1*(3) + +(-2)*(3)
#    1 -2 3
#  1    v v
# -2
#  3
# x1*(x2+x3+...+xn)+x2(x3+...+xn)+x3(x4+..xn)+xn-1(xn)
nums = list(map(int,input().split()))
partialSum = []
partialSum.append(nums[-1])

for start in range(1,n):
    partialSum.append(partialSum[start-1]+nums[n-1-start])

total = 0
for idx in range(n-1):
    total += nums[n-2-idx]*partialSum[idx]
print(total)

### key : 리스트로 이전 값들의 합들을 저장하고 다른 for loop으로 곱해줘서 O(2N)으로 만들어준 것
# https://ssafy-story.tistory.com/m/73?category=846431