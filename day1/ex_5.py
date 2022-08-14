txt = "Text messaging, or texting, is the act of composing and"
step = len(txt) // 3
i = 2
while step:
    txt = txt[:i:] + txt[i+1::]
    i += 2
    step -= 1
print(txt)
