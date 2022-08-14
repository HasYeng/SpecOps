text = open("text.txt", "r").read()
text_new = open("text_new.txt", "w")
text1 = text.title()
text_new.write(text1)

