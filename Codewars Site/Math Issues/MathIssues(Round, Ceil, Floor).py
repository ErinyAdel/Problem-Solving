def custom_round(num):
    n = str(num)
    if(n.count('.') == 1):
        if(int(n.split(".")[1]) >= 5):
            return int(n.split(".")[0]) + 1
        else:
            return int(n.split(".")[0])
    return num

def custom_ceil(num):
    n = str(num)
    if (n.count('.') == 1):
        if (int(n.split(".")[1]) >= 1):
            return int(n.split(".")[0]) + 1
        else:
            return int(n.split(".")[0])
    return num

def custom_floor(num):
    n = str(num)
    if (n.count('.') == 1):
        return int(n.split(".")[0])
    return num


print(custom_round(5))
print(custom_round(5.5))
print(custom_round(5.9))
print(custom_round(5.1))
print(custom_round(5.0))
print("----------")
print(custom_ceil(5))
print(custom_ceil(5.5))
print(custom_ceil(5.9))
print(custom_ceil(5.1))
print(custom_ceil(5.0))
print("----------")
print(custom_floor(5))
print(custom_floor(5.5))
print(custom_floor(5.9))
print(custom_floor(5.1))
print(custom_floor(5.0))