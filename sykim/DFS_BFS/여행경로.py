from collections import OrderedDict
def bfs(start_city, port, tickets):
    visit = []

    stack = []
    stack.append(start_city)

    temp=0
    while stack:
        city = stack.pop()
        temp+=1
        visit.append(city) # src

        if temp == len(tickets):
            visit.append(port[city][0])
            print(city, dest)
            print(f'port; {port}')
        else:
            dest = port[city][0] # dest, select by character order
            stack.append(port[city][0])  # dest , become new src
            print(city, dest)
            print(f'port; {port}')
            port[city].remove(dest)
    #         ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]
    return visit


def solution(tickets):
    p = set()
    for city_list in tickets:
        p.add(city_list[0])
        p.add(city_list[1])
    port_list = sorted(p)
    port = {p_name:[] for p_name in port_list}
    for pair in tickets:
        port[pair[0]].append(pair[1])

    port = OrderedDict(sorted(port.items()))
    for dest in port.values():
        dest.sort()
    answer = bfs('ICN', port,tickets)
    print(answer)
    return answer