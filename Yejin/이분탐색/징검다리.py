def solution(distance, rocks, n):
    answer = 0
    start = 0
    end = distance
    rocks.sort()
    
    while start <= end:
        mid = (start + end) // 2
        # mid가 거리의 최솟값이라고 가정
        remove = 0
        prev = 0
        for rock in rocks:
            if remove > n:
                break
            if rock - prev < mid:
                remove += 1
            else:
                prev = rock
            
        if remove > n:
            end = mid - 1
        else:
            answer = mid
            # 최솟값 중 가장 큰 값
            start = mid + 1
            
    return answer
    