from collections import deque

def solution(progresses, speeds):
    queue1 = deque(progresses)
    queue2 = deque(speeds)
    answer = []
    
    while queue1:
        for i in range(len(queue1)):
            queue1[i] += queue2[i]
            
        n = 0
        while queue1 and queue1[0] >= 100:
            queue1.popleft()
            queue2.popleft()
            n += 1

        if n > 0:
            answer.append(n)
                
    return answer
    