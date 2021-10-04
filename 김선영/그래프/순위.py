def solution(n, results):
    # 그래프 초기화
    winner_graph, loser_graph = dict(), dict()
    for i in range(1, n + 1):
        winner_graph[i], loser_graph[i] = set(), set()

    # winner_graph = {winner: loser set}
    # loser_graph = {loser: winner set}
    for winner, loser in results:
        winner_graph[winner].add(loser)
        loser_graph[loser].add(winner)

    for i in range(1, n + 1):
        # i한테 진 선수는 i를 이긴 선수한테 진 것
        for loser in winner_graph[i]:
            loser_graph[loser].update(loser_graph[i])
        # i한테 이긴 선수는 i한테 진 선수한테 이긴 것
        for winner in loser_graph[i]:
            winner_graph[winner].update(winner_graph[i])

    answer = 0
    for i in range(1, n + 1):
        # i한테 이기고, 진 애들을 모두 알게되면 순위를 알 수 있음
        if len(loser_graph[i]) + len(winner_graph[i]) == n - 1:
            answer += 1
    return answer