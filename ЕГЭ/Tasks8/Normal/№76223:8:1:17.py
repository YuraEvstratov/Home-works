# Определите количество шестеричных пятизначных чисел, в записи которых не менее двух цифр 5 и не более трёх нечетных цифр, меньших 4.
from itertools import *
count = 0
num = "012345"
for i in product(num, repeat=5):
    if i[0] != "0" and i.count("5") >= 2 and i.count("1") + i.count("3") <= 3:
        count += 1
print(count)