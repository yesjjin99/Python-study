import sys
from collections import defaultdict
input = sys.stdin.readline
trees = defaultdict(int)
total = 0
# key : 끝나지 않는 input 처리 방법! 두가지
for tree in sys.stdin:
    # tree = input()
    if tree == '\n':
        break
    else:
        trees[tree.rstrip()]+=1
        total += 1

trees = sorted(trees.items(), key=lambda x:x[0])
for k, v in trees:
    print(f'{k} {v/total*100:.4f}')