def f(nums: list) -> int:
    value = 0
    for i in nums:
        value ^= i
    return value
print(f([1, 2, 4, 2, 1]))
