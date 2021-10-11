def solution(answers):
    student_1 = [1, 2, 3, 4, 5]
    student_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    student_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    answer_num = [0, 0, 0]
    for idx in range(len(answers)):
        if student_1[idx % 5] == answers[idx]:
            answer_num[0] += 1
        if student_2[idx % 8] == answers[idx]:
            answer_num[1] += 1
        if student_3[idx % 10] == answers[idx]:
            answer_num[2] += 1

    answer = []
    max_value = max(answer_num)
    for i, n in enumerate(answer_num):
        if n == max_value:
            answer.append(i + 1)

    return answer