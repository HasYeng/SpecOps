num = 0
sum1 = 0
while num < 1000:
    if num % 3 == 0 or num % 5 == 0:
        sum1 += num
    num += 1
print(sum1)

