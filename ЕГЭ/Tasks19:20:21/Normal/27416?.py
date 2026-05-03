def f(i_1, i_2, m):
    if i_1 + i_2 >= 70:
        return m % 2 == 0
    if m == 0:
        return False
    h = [f(i_1 + 1, i_2, m - 1),
         f(i_1, i_2 + 1, m - 1),
         f(i_1 * 2, i_2, m - 1),
         f(i_1, i_2 * 2, m - 1),]
    return any(h) 
print("19:", *[i for i in range(1, 70) if f(7, i, 2)])
print("20:", *[i for i in range(1, 70) if f(7, i, 3) and not(f(7, i, 1))])
print("21:", min([i for i in range(1, 70) if f(7, i, 4) and not(f(7, i, 2))]))