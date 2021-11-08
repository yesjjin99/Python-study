def solution(participant, completion):
    part = dict()
    for p in participant:
        # 동명이인있는지 체크
        if p in part.keys():
            part[p] += 1
        else:
            part[p] = 1
            
    for c in completion:
        # 마라톤 완주한 선수 체크 후
        part[c] -= 1
        # 동명이인 존재할 수 있으니 카운트가 0인지 if문으로 확인 후 해시에서 제거
        if part[c] == 0:
            del part[c]
    
    return "".join(part.keys())
    