from collections import deque
answer = 0
def changable(begin, word):
    num = 0
    for i in range(len(word)):
        if begin[i] != word[i]:
            num += 1
    if num == 1:
        return True
    else:
        return False
    
def bfs(i, target, words):
    queue = deque([i])
    visited = []
    global answer
    
    while queue:
        i = queue.popleft()
        if changable(i, target) == True:
            answer += 1
            return answer
        for j in range(len(words)):
            if changable(i, words[j]) == True and words[j] not in visited:
                queue.append(words[j])
                visited.append(words[j])
                answer += 1
                break
    
def solution(begin, target, words):
    global answer
    if target in words:
        answer = bfs(begin, target, words)
        return answer
    else:
        return 0
        