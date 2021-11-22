from itertools import permutations

def solution(numbers):
    answer = 0
    nums = []
    for i in range(len(numbers)):
        nums += map(int, map("".join, permutations(list(numbers), i + 1)))
    nums = list(set(nums)) # for 문 안에서 set을 해주었더니 완벽히 중복 제거가 되지 않아서 밖으로 빼주고 list로 다시 만들어줌
        # permutations 이용해서 i개씩 순열 조합하여 모든 경우의 수 판정
        # 각 순열 조합 하나의 int형으로 map
        # 중복되는 수 map으로 제거 (속도 빨라짐)
    
    for i in range(len(nums)):
        isZero = False
        if nums[i] < 2:
            continue
        for j in range(2, int(nums[i]**0.5) + 1):
            if nums[i] % j == 0:
                isZero = True
                break
        if not isZero:
            answer += 1
            
    return answer
    