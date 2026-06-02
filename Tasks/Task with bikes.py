def gett_first_day(arr, target):
    left = 0
    right = len(arr) - 1
    k = 0
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] >= target:
            k = mid
            right = mid - 1
        else:
            left = mid + 1
    return k
def num_days(count_days, arr, price):
    bike1 = gett_first_day(arr, price)
    bike2 = gett_first_day(arr, price * 2)
    if bike1 != 0:
        bike1 += 1
    else:
        bike1 -= 1
    if bike2 != 0:
        bike2 += 1
    else:
        bike2 -= 1
    return bike1, bike2

print(num_days(6,[1, 2, 4, 4, 6, 8], 3))
print(num_days(6,[1, 2, 4, 4, 4, 4], 3))
print(num_days(6,[1, 2, 4, 4, 4, 4], 10))
