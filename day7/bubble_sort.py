def bubble_sort(lst):
    change = False
    for i in range(len(lst)):
        for j in range(len(lst) - 1 - i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                change = True
                if not change:
                    break
    return lst
lst = [1, 3, 2, 4, 8, 7]
print(bubble_sort(lst))
