def f(i_1, i_2, m):
    if i_1 + i_2 >= 82:
        return m % 2 == 0
    if m == 0:
        return False
    h = [f(i_1 + 1, i_2, m - 1),
         f(i_1, i_2 + 1, m - 1),
         f(i_1 * 4, i_2, m - 1),
         f(i_1, i_2 * 4, m -1)]
    return  any(h) if (m + 1) % 2 == 0 else all(h)
# print("19:",min([i for i in range(1, 82) if f(4, i, 2)]))
print("20:", *[i for i in range(1, 82) if f(4,i,3) and not f(4,i,1)]) 
print("21:", min([i for i in range(1, 82) if f(4,i,4) and not f(4,i,2)]))