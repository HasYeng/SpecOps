import string
def isPalindrome(s):
    s = s.translate(str.maketrans('', '', string.punctuation)).lower()
    s = s.replace(" ", "")
    print(s)
    return s == s[::-1]
print(isPalindrome("aa b b cc bb aa"))
