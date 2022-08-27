def str_move(string, num):
    move = num % len(string)
    new_str = string[-move::] + string[:-move:]
    return new_str


print(str_move("hello", 7))
