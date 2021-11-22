import heapq

def solution(operations):
    h = []

    for i in operations:
        alpha, n = i.split()
        if alpha == 'I':
            heapq.heappush(h, int(n))
        else: # D일 때(삭제)
            if len(h) > 0: # heap의 길이가 0 이상이어야 함
                if n == '1': # 최댓값 삭제 (Python은 최소힙만 구현되어 있으므로 nlargest로 최대힙 기능 구현)
                    #h.pop(h.index(heapq.nlargest(1, h)[0]))
                    h.remove(heapq.nlargest(1, h)[0])
                else: # 최솟값 삭제
                    heapq.heappop(h)

    if len(h) == 0:
        return [0, 0]
    else:
        return [heapq.nlargest(1, h)[0], h[0]]