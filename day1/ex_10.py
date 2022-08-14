def odd1(start, end):
    count = 0
    while start <= end:
        if start % 2 != 0:
            count += 1
        start += 1
    return count
print(odd1(1, 10))
