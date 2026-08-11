# 1)
# try:
#     num_1 = int(input("Input the number_1: "))
#     num_2 = int(input("Input the number_2: "))
#     rezult = num_1 / num_2
# except ZeroDivisionError:
#     print("Error: the namber must not be zero!")
# except ValueError:
#     print("Error: enter a number!")
# except Exception:
#     print("Unknown error")

# 2)
# try:
#     apartments = int(input("Input len apartments in one hous: "))
#     houses = int(input("Input len houses in city: "))
#     rezult = houses * houses

# except ValueError:
#     print("Input the number!!")
# except Exception:
#     print("Unknown error")

# else:
#     print(f"Len apartments in the city: {rezult}")

# 3)
# def arithmetic_mean(arr: list) -> int:
#     if not arr:
#         raise ValueError("List must not be empty")
#     return sum(arr) // len(arr)
# print(arithmetic_mean([]))

# 4)
# try:
#     file = open("data.txt", "r")
#     content = file.read()

# except FileNotFoundError:
#     print("File not found!")

# finally:
#     print("Closing file")
#     try:
#         file.close()
#     except NameError:
#         print("The file was not opened")
