def find(arr, k):
    left = 0
    max_value = 0
    l = []
    size = 0
    for right in range(len(arr)):
        size += 1
        while size >= k:
            for i in range(left, right + 1):
                l.append(arr[i])
            max_value = max(max_value,sum(l)/len(l))
            size -= 1
            l = []
            left += 1
    return max_value
print(find([1, 12, -5, -6, 50, 3], 4))
