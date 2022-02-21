import sys
sys.setrecursionlimit(10**9)

def postorder(left, right):
  if left > right:
    return
  else:
    mid = right + 1
    for i in range(left + 1, right + 1):
      if tree[i] > tree[left]:
        # i가 현재 노드(left)보다 크면 i를 기점으로 그 전은 왼쪽 서브 트리, 그 이후는 오른쪽 서브 트리로 구분
        mid = i
        break

    postorder(left + 1, mid - 1) # 왼쪽 노드(왼쪽 서브 트리)
    postorder(mid, right) # 오른쪽 노드(오른쪽 서브 트리)
    print(tree[left]) # 현재 노드

tree = []
while True:
  try: # 예외 발생하기 전까지 입력받아 append
    n = int(input())
    tree.append(n)
  except:
    break

postorder(0, len(tree) - 1)