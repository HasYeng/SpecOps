def lengthOfLastWord(s):
    lst = s.strip().split(" ")
    return(len(lst[-1]))
print(lengthOfLastWord("   fly me   to   the moon  "))

