from collections import defaultdict

def solution(tickets):
    answer = []
    routes = defaultdict(list)
    for t in tickets:
        routes[t[0]].append(t[1])
        routes[t[0]].sort(reverse = True)
    
    def dfs(depart):
        while depart:
            s = depart[-1]
            if not routes[s]:
                answer.append(depart.pop())
            else:
                depart.append(routes[s].pop())
    
    dfs(["ICN"])
    return answer[::-1]
    