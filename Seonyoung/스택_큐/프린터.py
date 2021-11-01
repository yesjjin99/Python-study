from collections import deque


def solution(priorities, location):
    queue = deque([(p, i) for i, p in enumerate(priorities)])

    answer = 0

    while True:
        max_p = max(queue, key=lambda x: x[0])
        p, i = queue.popleft()
        if p == max_p[0]:
            answer += 1
            if i == location:
                break
        else:
            queue.append((p, i))
    return answer