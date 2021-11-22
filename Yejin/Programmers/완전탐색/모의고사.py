def solution(answers):
    answer = []
    corrects = [0 for i in range(3)]
    s1 = [1,2,3,4,5]
    s2 = [2,1,2,3,2,4,2,5]
    s3 = [3,3,1,1,2,2,4,4,5,5]
    
    for i in range(len(answers)):
        if answers[i] == s1[i % len(s1)]:
            corrects[0] += 1
        if answers[i] == s2[i % len(s2)]:
            corrects[1] += 1
        if answers[i] == s3[i % len(s3)]:
            corrects[2] += 1
    
    top = max(corrects)
    for i in range(len(corrects)):
        if corrects[i] == top:
            answer.append(i + 1)
            
    return answer
    