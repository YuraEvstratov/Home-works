def count_nums(n):
    count = 0
    while n > 0:
        count += n % 10
        n = n // 10
    return count
l = []
for n in range(10000):
    x = bin(n)[2:]
    if count_nums(n) % 2 != 0:
        x += "1"
    else:
        x +="0"
    e = int(x, 2)
    if count_nums(e) % 2 != 0:
        x += "1"
    else:
        x +="0"
    p = int(x, 2)
    if count_nums(n) % 2 != 0:
        x += "1"
    else:
        x +="0"
    R = int(x, 2)
    if R > 1028:
        l.append(R)
print(min(l))   
    