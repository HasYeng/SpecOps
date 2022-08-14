def intersection(nums1, nums2):
    inter = []
    for i in nums1:
        if i in nums2 and i not in inter:
            inter.append(i)
    return(inter)
print(intersection([4, 5, 6, 7], [4, 6, 8]))
