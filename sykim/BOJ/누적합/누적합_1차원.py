arr = list(range(5))

# append
value = 0
append_sum = [value]

for i in arr:
    value += i
    append_sum.append(value)

print(append_sum)

# memoization
memo_sum = [0] * (len(arr)+1)
for i in range(1,len(arr)+1):
    memo_sum[i] = memo_sum[i-1] + arr[i-1]

print(memo_sum)