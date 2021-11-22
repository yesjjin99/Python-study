# https://blog.naver.com/PostView.nhn?isHttpsRedirect=true&blogId=jaeyoon_95&logNo=221872563653&categoryNo=74&parentCategoryNo=0&viewDate=&currentPage=1&postListTopCurrentPage=1&from=postView
# KrusKal 알고리즘

def solution(n, costs):
    answer = 0
    costs.sort(key = lambda x: x[2])
    connected = set([costs[0][0]])
    
    while len(connected) != n:
        for i, cost in enumerate(costs):
            # 두 섬이 이미 연결되어 있는 경우 continue
            # 이미 sort() 했기 때문에 이 경우 더 작은 값이 후에 들어올 일은 없음
            if (cost[0] in connected) and (cost[1] in connected):
                continue
            # 둘 중 하나만 연결되어 있는 경우
            if (cost[0] in connected) or (cost[1] in connected):
                answer += cost[2]
                connected.add(cost[0])
                connected.add(cost[1])
                costs.pop(i)
                break
                
    return answer
    