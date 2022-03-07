'''
start, end 사이의 홀수 개수(cnt)를 세면서,
홀수 개수가 K개 이하인 경우 end를 증가시키고 보내고,
홀수 개수가 K개를 초과하게 되면 start를 증가시킨다
'''

N, K = map(int, input().split())
seq = list(map(int, input().split()))

cnt = 0  # 홀수의 개수
ans = 0  # 짝수로 이루어져 있는 연속한 부분 수열 중 가장 긴 길이 (최종 답)
t_ans = 0  # start, end 사이의 짝수 개수
start, end = 0, 0
while start < N:
    # 홀수 개수가 K개 이하 & end가 배열 끝에 다다르지 않았을 경우
    while cnt <= K and end < N:
        if seq[end] % 2 == 0:  # 짝수인 경우
            t_ans += 1
        else:  # 홀수인 경우
            cnt += 1
        end += 1

    ans = max(ans, t_ans)

    if seq[start] % 2 == 0:  # 짝수인 경우
        t_ans -= 1
    else:  # 홀수인 경우
        cnt -= 1
    start += 1

print(ans)