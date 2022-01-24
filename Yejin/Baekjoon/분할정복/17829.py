n = int(input())
arr = []

for _ in range(n):
  row = list(map(int, input().split()))
  arr.append(row)

def pooling(arr, n):
  if n == 1:
    return arr[0][0]

  new_arr = [[] for _ in range(n // 2)]
  for i in range(0, n, 2):
    for j in range(0, n, 2):
      new_arr[i // 2].append(sorted([arr[i][j], arr[i][j+1], arr[i+1][j], arr[i+1][j+1]])[2])

  return pooling(new_arr, n // 2)

print(pooling(arr, n))