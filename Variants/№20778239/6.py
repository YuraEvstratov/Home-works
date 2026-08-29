l = 0
for n in range(34722222, 45138889):
    a = n % 3
    b = (4 * n + a) % 5
    R = 32 * n + 8 * a + b
    if 1111111110 <= R <= 1444444416:
        l += 1
print(l)
