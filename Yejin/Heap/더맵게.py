import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0
    
    while scoville[0] < K:
        num = heapq.heappop(scoville) + (heapq.heappop(scoville) * 2)
              # scoville[0] + (scoville[1] * 2)
        heapq.heappush(scoville, num)
        answer += 1
        
        if scoville[0] < K and len(scoville) == 1:
            return -1
        
    return answer
    