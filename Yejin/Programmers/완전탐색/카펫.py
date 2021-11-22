def solution(brown, yellow):
    answer = []
    x = 0
    y = 0
    for i in range(1, int(yellow**0.5) + 1):
        if yellow % i == 0:
            y = i
            x = yellow // i
            brown_tmp = (x + 2) * 2 + y * 2
            if brown == brown_tmp:
                answer.append(x + 2)
                answer.append(y + 2)
    
    return answer
    