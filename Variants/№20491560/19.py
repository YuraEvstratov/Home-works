l = []
def trinity(n):
    s = ""
    while n != 0:
        s += str(n % 3)
        n = n // 3
    return s[::-1]
def count_nums(n):
    count = 0
    while n != 0:
        count += n % 10
        n = n // 10
    return count
for n in range(1, 10000):
    x = trinity(n)
    if n % 3 == 0:
        x += x[-2:]
    else:
        x += trinity((count_nums(int(x)) * 3))
    R = int(x, 3)
    if 820< R < 850:
        l.append(R)
print(l)
