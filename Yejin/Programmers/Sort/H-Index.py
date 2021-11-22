def solution(citations):
    # h번 이상 인용된 논문 h편일 때의 h 최댓값을 찾아야 하므로 내림차순으로 정렬하여 큰 값부터 비교해야 함
    # 6 : 1번 이상 인용된 논문 1편
    # 5 : 2번 이상 인용된 논문 2편
    # 3 : 3번 이상 인용된 논문 3편
    # 1 : 4번 이상 인용된 논문 4편 (X) -> 멈춤
    citations.sort(reverse = True)
    for i, c in enumerate(citations):
        if i >= c: # 인용 횟수와 편수 비교
            return i
    
    # 모든 인용 횟수가 논문 n편보다 커 반복문을 그대로 빠져나온 경우 h의 최댓값은 n이 됨
    # ex.) [11, 22, 33, 44, 55]
    return len(citations)