def findMaxConsecutiveOnes(nums):
    lst = []
    count = 0
    for i in nums:
        if i == 1:
            count += 1
        if i == 0:
            lst.append(count)
            count = 0
    lst.append(count)
    return max(lst)
print(findMaxConsecutiveOnes([1,1,0,1,1,1]))
