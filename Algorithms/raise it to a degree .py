try:
    len_nums = int(input("Enter the len of numbers "))
except ValueError:
    print("Error: enter a number!")
else:
    if len_nums < 0:
        raise ValueError("The number must be positive")
    arr = []
    for i in range(len_nums):
        try:
            num = int(input("Enter the number "))
            arr.append(num)
        except ValueError:
            print("Error: enter a number!")
            break
    else:
        degree = int(input("Enter the degree "))
        for i in range(0, len_nums):
            print(arr[i] ** degree) 