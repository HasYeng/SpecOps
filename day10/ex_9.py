num = 0
for i in range(999, 100, -1):
    for j in range(i, 100, -1):
        x = i * j
        if str(x) == str(x)[::-1] and num < x:
            num = x
print(num)
