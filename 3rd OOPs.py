#There are two types variable
#1)Instance variable - It can be changed respectively to object
#2)Class/Static variable - It can be changed in common to objects. Its declared inside class but outside of define function



class Car:

    wheels = 4  #Class/Static variable

    def __init__(self):
        self.mil = 10    #Instance variable
        self.com = "BMW"   #Instance variable


c1 = Car()
c2 = Car()

c1.mil = 8 #Changes but respective to its object

Car.wheels = 5   #Changes and affect all object

print(c1.com , c1.mil , c1.wheels)
print(c2.com , c2.mil , c2.wheels)