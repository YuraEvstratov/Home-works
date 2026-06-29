l = []
for n in range(10000):
    x = bin(n)[2:]
    x += bin(n % 4)[2:]
    R  = int(x, 2)
    l[R] = 1
maxi = 0
for i in range(1000):
    maxi = max( maxi, sum(l[i : i + 65]))
print(maxi)
