def palindrome(num):
    if num < 0:
      return False
    num_save = num
    new_num = 0
    while num:
        new_num = new_num*10 + num % 10
        num //= 10
    return new_num == num_save
print(palindrome(434))
