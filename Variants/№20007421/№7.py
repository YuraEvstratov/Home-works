def trinity(n):
    k = ""
    while n > 0:
        k = str(n % 3) + k
        n = n // 3
    return k
def summa(n):
    k = 0
    while n > 0:
        k += n % 10
        n = n // 10
    return k
l =[]
for n in range(1,1000):
    x = trinity(n)
    if n % 3 == 0:
        x += x[-2:]
    else:
        x += trinity(summa(int(x)) * 3)   
    R = int(x, 3)
    if 890 < R < 930:
        l.append(R)
print(l)