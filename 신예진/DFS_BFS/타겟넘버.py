answer = 0
def solution(numbers, target):
    l = len(numbers) 
    
    def dfs(i, result):
        if i == l:
            if result == target:
                global answer
                answer += 1
        else:
            dfs(i+1, result+numbers[i])
            dfs(i+1, result-numbers[i])
            
    dfs(0, 0)
    return answer
