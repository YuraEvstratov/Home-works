def f(n):
    if n == 0:
        return 0
    if n % 2 != 0:
        return f(n - 1) + 1
    if n > 0 and n % 2 == 0:
        return f(n / 2)
l = 1
k = 0
while l != 1000000000:
    if f(l) == 3:
        k += 1
    l += 1
print(k)
