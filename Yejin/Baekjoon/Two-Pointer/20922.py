n, k = map(int, input().split())
arr = list(map(int, input().split()))
list = [0] * (max(arr) + 1) # 중복 카운트
# two-pointer
s, e, answer = 0, 0, 0

while e < n:
  if list[arr[e]] < k:
    list[arr[e]] += 1
    e += 1
  else:
    list[arr[s]] -= 1 # 카운트에서 제거
    s += 1
  answer = max(answer, e - s) # 최댓값 갱신

print(answer)