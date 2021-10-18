def solution(people, limit):
    answer = 0
    people.sort()

    # Point
    # 정렬
    # (가장 가벼운 사람, 가장 무거운 사람) > limit: 가장 무거운 사람은 짝이 없다-> answer += 1

    start, end = 0, len(people) - 1
    while start <= end:
        if people[start] + people[end] <= limit:
            start += 1
        end -= 1
        answer += 1

    return answer