def strmove(string, num):
    move = num % len(string)
    new_str = string[-move::] + string[:-move:]
    return new_str
strmove("hello", 7)
