def two_index(arr: list, k: int) -> bool:
    if not list or not k:
        return False
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j] and abs(i - j) <= k:
                return True
    return False
print(two_index([1, 2, 3, 1], 3))
print(two_index([1, 0, 1, 1], 1))
print(two_index([1, 2, 3, 1, 2, 3], 2))