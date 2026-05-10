def f(i_1, i_2, m):
    if i_1 + i_2 <= 20 :
        return m % 2 == 0
    if m == 0:
        return False
    h = [f(i_1 - 1, i_2, m - 1),
         f(i_1, i_2 - 1, m - 1),
         f(i_1 // 2, i_2, m - 1),
         f(i_1, i_2 // 2, m - 1)]
    return any(h) 
print("19:", min([i for i in range(100, 10, - 1) if f(10, i, 2)]))
# print("20:", *[i for i in range(1, 69) if f(10, i, 3) and not f(10, i , 1)])
# print("21:", min([i for i in range(1, 69) if f(10, i, 4) and not f(10, i , 2)]))