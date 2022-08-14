txt = open("text.txt", "r").read()
count = 0
for i in txt:
    if i.isprintable():
        count += 1
print(count)

