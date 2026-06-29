try:
    n = int(input("Input len clubs: "))
    all_clubs = set()
    for i in range(n):
        all_clubs.add(str(input("Club`s name: ")))
    print(*all_clubs)
except ValueError:
    print("Error: Invalid input!")
