class Student:
    def __init__(self, height = 170):
        self.height = height


vasya = Student()
petya = Student(height=180)

print(vasya.height)
print(petya.height)


