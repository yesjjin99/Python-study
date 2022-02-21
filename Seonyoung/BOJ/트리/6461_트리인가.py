'''
< 문제 조건 >
1. 들어오는 간선이 하나도 없는 단 하나의 노드가 존재한다. 이를 루트(root) 노드라고 부른다.
2. 루트 노드를 제외한 모든 노드는 반드시 단 하나의 들어오는 간선이 존재한다.
3. 루트에서 다른 노드로 가는 경로는 반드시 가능하며, 유일하다. 이는 루트를 제외한 모든 노드에 성립해야 한다.

< 풀이 >
- 1번 조건 -> 들어오는 간선이 0개인 노드가 1개만 존재
- 2&3번 조건 -> 루트노드 제외하고 나머지 노드는 들어오는 간선이 1개

1.노드에 들어오는 간선의 개수를 세는 dict를 생성
dict = {node: 들어오는 간선의 개수}
2. dict내에서 1개의 노드(root)만 0(value)를 가지고 나머지 노드는 모두 1(value)을 가져야만 tree임
- 예외처리 : 노트가 0개인 트리도 트리임
'''

case = 1
ckt = True
while ckt:
    n = list()
    while True:  # 테스트 입력 데이터 저장
        tmp = list(map(int, input().split()))
        if tmp[-2:] == [0, 0]:
            n.extend(tmp[:-2])
            break
        elif tmp == [-1, -1]:
            ckt = False
            break
        n.extend(tmp)

    if not ckt:
        continue

    # dict에 들어오는 간선 저장
    node_d = dict()
    for i in range(0, len(n) - 1, 2):
        u, v = n[i], n[i + 1]  # u: 시작 노드, v: 도착 노드

        if u not in node_d.keys():  # 시작 노드 u도 dict에 저장해줌 (root 추적을 위하여)
            node_d[u] = 0

        # 도착 노드 v를 dict에 저장
        if v in node_d.keys():
            node_d[v] += 1
        else:
            node_d[v] = 1

    root, dup = 0, 0
    for node in node_d.keys():
        if node_d[node] == 0:
            root += 1
        elif node_d[node] != 1:
            dup += 1

    if len(n) == 0:  # 예외처리(노드의 개수가 0개인 트리)
        root = 1  # root를 1로 만들어줘서 tree 조건을 갖추게 조정해줌

    if root == 1 and dup == 0:
        print(f'Case {case} is a tree.')
    else:
        print(f'Case {case} is not a tree.')
    case += 1