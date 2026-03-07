def merge(first: tuple, second: tuple) -> tuple:
    if first[-1] < second[0]:
        return first + second
    return second + first
print(merge((1, 2), (3, 4, 5)))
print(merge((3, 4, 5), (1, 2)))