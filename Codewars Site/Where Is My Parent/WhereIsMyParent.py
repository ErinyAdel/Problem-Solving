def findChildren(dancingBrigade):
    lst = []
    for i in dancingBrigade.lower():
        lst.append(i)
    lst = sorted(lst)

    dict = {}
    for i in lst:
        if i not in dict:
            dict[i] = 0
        else:
            dict[i] += 1

    res = ""
    for k, v in dict.items():
        if v == 0:
            res += k.upper()
        else:
            res += k.upper()
            for i in range(v):
                res += k

    return res

print(findChildren("beeeEBb"))
print(findChildren("uwwWUueEe"))
print(findChildren("abBA"))