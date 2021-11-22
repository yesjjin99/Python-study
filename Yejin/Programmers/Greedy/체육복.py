def solution(n, lost, reserve):
    Lost = set(lost) - set(reserve)
    Reserve = set(reserve) - set(lost)
    answer = n - len(Lost)
    # 체육복 있는 학생들의 수
    
    for l in Lost:
        if l - 1 in Reserve:
            Reserve.remove(l - 1)
            answer += 1
        elif l + 1 <= n and l + 1 in Reserve:
            Reserve.remove(l + 1)
            answer += 1
            
    return answer


# 여벌 체육복이 있는 학생만 빌려줄 수 있기 때문에
# 여벌 체육복이 있는 학생이 분실한 경우, 먼저 여벌 체육복이 있는 학생 리스트에서 제외하여 따로 처리하면 문제 해결됨
# -> 그러므로 먼저 set으로 중복 제외 처리함

# pop은 index로 제거 가능
# remove는 값으로 제거 가능