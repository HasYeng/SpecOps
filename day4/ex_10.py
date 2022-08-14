def searchRange(nums, target):
    start = 0
    end = len(nums) - 1
    while start <= end:
        mid = (start + end) // 2
        if nums[start] == nums[end] == target:
            return [start, end]
        elif nums[mid] < target:
            start = mid + 1
        else:
            if nums[start] != target: 
                start += 1
            if nums[end] != target: 
                end -= 1 
    return [-1, -1]

nums = [5,7,7,8,8,10]
target = 88
print(searchRange(nums, target))
