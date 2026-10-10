# A basic class and object
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(f"{self.name}: {self.marks}")

student1 = Student("Ram", 85)
student1.display()
