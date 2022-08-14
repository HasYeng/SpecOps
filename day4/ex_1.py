def targ(target):
    lst = []
    for i in range(1, target[-1] + 1):
      if i in target:
        lst.append("push")
      else:
        lst.append("push")
        lst.append("pop")
    return(lst)
targ([1, 2, 4])
