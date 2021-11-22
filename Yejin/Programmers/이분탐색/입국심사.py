def solution(n, times):
    answer = 0
    m = len(times)
    times.sort() # 이분탐색 위해 sort
    
    start = 1
    end = times[m - 1] * n # 최대 걸릴 수 있는 시간
    # Binary Search
    while start <= end:
        mid = (start + end) // 2
        sum = 0
        for time in times:
            sum += mid // time
        # 배열 times의 작은 값(빠른 심사대)부터 mid(시간) 동안 총 몇 명 받을 수 있는지 계산 후 더함
        # 결과적으로 빠른 심사대일수록 mid(시간) 동안 받을 수 있는 최대 사람 받은 것
        
        if sum >= n:
            answer = mid
            # 일단 answer에 mid 넣어놓고 가장 최솟값 나올 때까지 반복
            end = mid - 1
        else:
            start = mid + 1
    return answer
