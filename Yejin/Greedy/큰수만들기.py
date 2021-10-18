def solution(number, k):
    answer = ''
    nums = []
    
    for i, n in enumerate(number):
        while nums and nums[-1] < n and k > 0:
            nums.pop()
            k -= 1
        if k == 0:
            nums += number[i:]
            break
        nums.append(n)
    
    # k > 0일 때 반복문에서 빠져나왔을 경우 k만큼 뒤에서부터 숫자를 빼줌
    if k > 0:
        nums = nums[:-k]
        
    answer = "".join(nums)
    return answer
    