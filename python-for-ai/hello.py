#updates

class IBilim:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

student1 = IBilim("Nurdos", '11B')
print(student1.name, student1.grade)
