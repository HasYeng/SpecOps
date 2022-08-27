def dev_by_3_5(num):
    sum1 = 0
    while num:
        if num % 3 == 0 or num % 5 == 0:
            sum1 += num
        num -= 1
    return sum1


print(dev_by_3_5(999))
