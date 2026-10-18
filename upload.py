class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def show_info(self):
        print("Name:", self.name)
        print("Marks:", self.marks)


s1 = Student("Ali", 85)
s1.show_info()