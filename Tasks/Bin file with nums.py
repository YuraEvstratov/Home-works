def create_bin_file(arr: list):
    name = "/tmp/file.bin"

    with open(name, "wb") as f:
        for num in arr:
            f.write(num.to_bytes(4, "little"))  

    with open(name, "rb") as f:
        content = f.read()
        print(content)

        f.seek(0)
        nums = []
        while True:
            value = f.read(4)
            if not value:
                break
            nums.append(int.from_bytes(value, "little"))
    return nums

print(create_bin_file([12, 31, 131, 32]))