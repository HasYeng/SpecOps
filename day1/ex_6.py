file_t = open("textfile.txt", "r")
dict_t = {}
count = 0
for lines in file_t:
    words = lines.strip().split(" ")
    for word in words:
        if word in dict_t:
            dict_t[word] += 1
        else:
            dict_t[word] = 1
print(dict_t)
