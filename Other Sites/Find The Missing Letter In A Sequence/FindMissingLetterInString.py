def findTheMissing(text):
    missing = None
    txtList = []
    for i, t in enumerate(text):
        txtList.append(t)
        if i != 0:
            n = ord(text[i])
            if n != ord(text[i-1]) + 1:
                missing = chr(ord(text[i-1])+1)
                #
                txtList.insert(i, missing)
                break
    # For checking is the it is a valid sequence or not.
    seq = []
    isValid = False
    for t in txtList:
        seq.append(ord(t))

    isValid = all(i == j - 1 for i, j in zip(seq, seq[1:]))

    return missing if isValid else "Isn't Valid"


print(findTheMissing("abcef")) #d
print(findTheMissing("abcdeghi"))#f
print(findTheMissing("defgi"))#h
print(findTheMissing("xyz"))#none
print("---------")
print(findTheMissing("cba"))# not valid
print("---------")
print(findTheMissing("fecba")) #not valid
print(findTheMissing("ihgedcba"))#not valid
print(findTheMissing("igfed"))#not valid
print(findTheMissing("zyx"))#not valid