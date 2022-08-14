count = 0
n = 3
lst = [1, 2]
while n < 4000000:
    lst.append(n)
    n = lst[-2] + lst[-1]
for i in lst:
    if i % 2 == 0:
        count += i
print(count)
