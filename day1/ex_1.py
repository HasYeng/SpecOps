nums = open("num.txt", "r")
count = 0
for i in nums:
    sum1 = i.split(" ")
    sum2 = list(map(int, sum1))
    count += sum(sum2)
print(count)
