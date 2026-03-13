def build_string(separator: str, **kwargs) -> str:
    rezult = ""
    count = 0
    for key, value in kwargs.items():
        if count == len(kwargs) - 1:
            rezult +=  str(key) + "=" + str(value)
        else:
            rezult +=  str(key) + "=" + str(value) + separator 
        count += 1
    return rezult
print(build_string("-", animal="cat", sound="meow"))
print(build_string(" | ", first=1, second=2, third=3, extra="data"))
print(build_string(", ", name="Alice", age=30, city="London"))