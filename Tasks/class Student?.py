class Student:
    k = 0
    def __init__(self, name = str):
        self.name = name
        k += 1

    def __del__(self):
        k -= 1
    def get_total(k) -> int:
        return k
    
s1 = Student("Alice")
s2 = Student("Bob")
s3 = Student("Charlie")
print(f"Total: {Student.get_total()}")  