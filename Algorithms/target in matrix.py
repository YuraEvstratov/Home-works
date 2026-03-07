def searchMatrix(matrix: list[list[int]], target: int) -> bool:
    global_left = 0
    global_right = len(matrix) - 1
    global_mid = (global_left + global_right) // 2
    left = 0
    right = len(matrix[global_mid]) - 1
    if target > matrix[-1][-1] or target < matrix[0][0]:
        return False
    while left <= right:
        mid = (left + right) // 2
        if matrix[global_mid][mid] == target:
            return True
        elif matrix[global_mid][0] > target < matrix[global_mid][-1]:
            global_mid -= 1
            left = 0
            right = len(matrix[global_mid]) - 1
        elif matrix[global_mid][0] < target > matrix[global_mid][-1]:
            global_mid += 1
            left = 0
            right = len(matrix[global_mid]) - 1
        if matrix[global_mid][mid] < target:
            left = mid + 1
        elif matrix[global_mid][mid] > target:
            right = mid - 1
    return False
print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],3))
print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],-3))
print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],17))
print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],600))
print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],20))