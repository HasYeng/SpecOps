def insertion_sort(lst):
    for i in range(1, len(lst)):
        j = i
        while lst[j] < lst[j-1] and j > 0:
            lst[j], lst[j - 1] = lst[j - 1], lst[j]
            j -= 1
    return lst


print(insertion_sort([3, 5, 99, 78, 4, 16, 17, 3]))

