count = 2
n = 3
lst = [1, 2]
while n < 4000000:
    lst.append(n)
    n = lst[-2] + lst[-1]
    if n % 2 == 0:
        count += n
print(count)
