# inner class
# You can create a class inside a class

# Eg-
class Student:

    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop()  # variable related to inner class

    def show(self):
        print(self.name, self.rollno)
        self.lap.show()

    class Laptop:  # Inner class

        def __init__(self):  # Inner class constructor
            self.brand = "Apple"
            self.model = "Macbook Air"
            self.variant = "Core i5"

        def show(self):
            print(self.brand, self.model, self.variant)


s1 = Student('Pratik', 2)
s2 = Student('Divyesh', 3)

s1.show()

lap1 = Student.Laptop()  # object related to inner class directly can be created without inner class variable using
#                          in outside class [__init__ ] you can directly call it

# s1.lap.brand      #Object
# lap1 = s1.lap     #Object for laptop
# lap2 = s2.lap

# print(id(lap1))
# print(id(lap2))
