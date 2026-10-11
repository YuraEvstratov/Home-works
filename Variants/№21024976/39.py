l = []
import string
s = "012345678"
for A in range(10000):
    for x in s:
        M = int("842" + x + "5", 9)
        N = int("8" + x + "725", 9)
        if (M + A) % N == 0:
            l.append(A)
print(min(l))
