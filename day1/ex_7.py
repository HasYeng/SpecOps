def square(num):
    return num ** 2
lst = [1, 3, 5, 6, 3, 9, -5, -6]
sqlst = list(map(square, lst))
sqlst.sort()
print(sqlst)

