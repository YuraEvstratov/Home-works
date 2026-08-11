def f(i_1, i_2, m):
    if i_1 + i_2 >= 48:
        return m % 2 == 0
    if m == 0:
        return False
    if i_1 > i_2:
        h = [f(i_1 + 1, i_2, m - 1),
             f(i_1 + 2, i_2, m - 1),
             f(i_1 + 3, i_2, m - 1),
             f(i_1, i_2 * 2, m - 1),]
    if i_2 > i_1:
        h = [f(i_1, i_2 + 1, m - 1),
             f(i_1, i_2 + 2, m - 1),
             f(i_1, i_2 + 3, m - 1),
             f(i_1 * 2, i_2, m - 1),]
    if i_2 == i_1:
            h = [f(i_1, i_2 + 1, m - 1),
                 f(i_1, i_2 + 2, m - 1),
                 f(i_1, i_2 + 3, m - 1),
                 f(i_1 * 2, i_2, m - 1),
                 f(i_1 + 1, i_2, m - 1),
                 f(i_1 + 2, i_2, m - 1),
                 f(i_1 + 3, i_2, m - 1),
                 f(i_1, i_2 * 2, m - 1),]
    return any(h) if (m + 1) % 2 == 0 else all(h)
print('19:', min([s1+s2 for s1 in range(1, 100) for s2 in range(1, 100) if f(s1, s2, 2)]))
print('20:', *[s2 for s2 in range(1, 48) if f(13, s2, 3) and not f(13, s2, 1)])
print('21:', *[s2 for s2 in range(1, 48) if f(39, s2, 4) and not f(39, s2, 2)])