# https://whwl.tistory.com/93
# https://this-programmer.tistory.com/379?category=754239
# 나중에 또 풀어볼 것ㅠㅠ 

def solution(name):
    move = [min(ord(i) - ord('A'), ord('Z') - ord(i) + 1) for i in name]
    # 각 자리의 알파벳을 만들기 위해 움직여야 하는 최소한의 조이스틱 가동횟수 구하기
    idx, answer = 0, 0
    
    while True:
        answer += move[idx]
        # answer에 현재 idx에 해당하는 move 더함
        move[idx] = 0
        # 해당 idx의 알파벳 조정이 완료된 경우 0으로 만들어주어 표시해줌
        if sum(move) == 0:
            return answer
        # 모든 알파벳이 조정된 경우(move의 sum이 0인 경우) 반복을 끝내고 결과를 return 하도록
        
        left, right = 1, 1
        # idx에서 좌우로 움직여 먼저 A를 만나는 방향을 찾음
        while move[idx - left] == 0:
            left += 1
        while move[idx + right] == 0:
            right += 1
        
        answer += left if left < right else right
        idx += -left if left < right else right
        
    return answer
    