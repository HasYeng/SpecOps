lst = [3,1,2,4,1]
lst_evens, lst_odds = [], []
for i in lst:
    if i % 2 == 0:
        lst_evens.append(i)
    else:
        lst_odds.append(i)
print(lst_evens+lst_odds)
