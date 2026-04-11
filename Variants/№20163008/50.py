def f(n):
    if n <= 2:
        return 1
    else:
        return 2 * f(n - 1) + f(n - 2)
print(f(7))