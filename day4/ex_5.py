def sumOfUnique(nums):
    sum_of_uniques = 0
    for i in nums:
        if nums.count(i) == 1:
            sum_of_uniques += i
    return sum_of_uniques
print(sumOfUnique([1, 2, 3, 4, 4]))
