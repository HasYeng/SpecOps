def selection_sort(lst):
    for i in range(len(lst)):
        min_i = i
        for j in range(i + 1, len(lst)):
            if lst[min_i] > lst[j]:
                min_i = j
        lst[i], lst[min_i] = lst[min_i], lst[i]
    return lst

print(selection_sort([3, 2, 5, 6, 1, 5]))
