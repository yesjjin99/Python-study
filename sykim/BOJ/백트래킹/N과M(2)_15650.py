# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
# 고른 수열은 오름차순이어야 한다. >> 1부터 증가하면서 시작하도록 backtracking 함으로써 보장
n, m = list(map(int, input().split()))
result = []

def dfs(start):
    if len(result) == m:
        # M개를 고른 수열 -> len(m)일 때 return

        print(' '.join(map(str,result)))
        # return
    # for i in range(1, n + 1):
    for i in range(start, n+1):
        if i not in result:
            result.append(i)
            # dfs()
            dfs(i+1)
            # 끝나면 pop해주고 다음 숫자가 result로 들어감
            result.pop()
# dfs()
dfs(1)

# 백트래킹
# - 길을 가다가 이 길이 아닌 것 같으면 왔던 길로 되돌아가 다른 경로로 진행
# - 보통 재귀로 구현하며 조건이 맞지 않으면 종료한다.
# - DFS(깊이 우선 탐색) 기반
#https://jiwon-coding.tistory.com/34