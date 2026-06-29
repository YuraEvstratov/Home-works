def find(arr, k):
    left = 0
    max_value = 0
    summa = 0
    size = 0
    for right in range(len(arr)):
        size += 1
        summa += arr[right]
        while size >= k:
            max_value = max(max_value,summa / k)
            size -= 1
            summa -= arr[left]
            left += 1
    return max_value
print(find([1, 12, -5, -6, 50, 3], 4))
