import sys
input = sys.stdin.readline

nums =  int(input())
lists = list(map(int,input().rstrip()))
# lists = list(map(int,input().split()))
assert nums == len(lists)
totalSum=sum(lists)
print(totalSum)
# a = input().split()
# print(a)
# lists = list(map(int,a))
# print(lists)

# key: input().rstrip()과 input().split() 차이