'''
반복문을 road의 길이만큼 반복하는데(마지막 도시의 기름 가격은 아무 영향을 주지 않기 때문에 고려하지 않아도 된다)

i 도시에서 다음(next) 도시까지 이동하기 위하여 필요한 기름을 어디에서 넣을지 결정하기 위해서
해당 i 도시의 기름 가격과 이전 도시 중 가장 가격이 싼 기름 가격(gas[pre])를 비교한다
1. 만약 gas[i] > gas[pre] 라면, pre 도시의 기름을 넣는게 이득이기 때문에 pre 도시에서 i->next 도시 거리만큼 기름을 넣고,
2. gas[i] <= gas[pre] 라면, 현재 도시에서 기름을 넣는게 이득이기 때문에 i 도시에서 next 도시까지의 거리만큼 기름을 넣는다
    이 경우, 가장 싼 기름 i가 된것이므로 pre를 i로 업데이트 해준다
'''

N = int(input())
road = list(map(int, input().split())) # 도로의 길이
gas = list(map(int, input().split())) # 기름 가격

cost = 0
pre = 0
for i in range(N-1):
    if gas[i] > gas[pre]:
        cost += (gas[pre]*road[i])
    else:
        cost += (gas[i]*road[i])
        pre = i

print(cost)