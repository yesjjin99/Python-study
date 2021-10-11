def solution(brown, yellow):
    answer = []

    total = brown + yellow
    x, y = 0, 0

    # total의 약수를 찾는 과정
    for i in range(3, total):
        if total % i == 0:
            x = i
            y = total // i
            if (x - 2) * (y - 2) == yellow:
                # [가로, 세로], 단 가로>=세로
                answer.append(y)
                answer.append(x)
                break
    return answer