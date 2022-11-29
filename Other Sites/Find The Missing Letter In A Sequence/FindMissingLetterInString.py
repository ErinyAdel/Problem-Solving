def findTheMissing(text):
    missing = None
    for i, t in enumerate(text):
        if i != 0:
            n = ord(text[i])
            #print(n, ord(text[i-1])+1)
            if n != ord(text[i-1]) + 1:
                missing = chr(ord(text[i-1])+1)
                break
    return missing


print(findTheMissing("abcef")) #d
print(findTheMissing("abcdeghi"))#f
print(findTheMissing("defgi"))#h
print(findTheMissing("xyz"))#none