# Types of methods
# 1)Instance method
# 2)Class method
# 3)Static method


# 1) Instance method - It can be defined as method working with Object
# Inside it there are two methods
# 1.Accessor method- Related to get the value(getters)
# 2.Mutators method - It is used to set the value(setters)

class Student:

    school = 'Telusko'

    def __init__(self, m1, m2, m3): #Instance method related to object

        self.m1 = m1      #declared by using self
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return (self.m1 + self.m2 + self.m3)/3

    def get_m1(self):  #Acces method
        return self.m1
    def set_m1(self,value):  #Mutator method
        self.m1 = value.m2

s1 = Student(23,44,55)
s2 = Student(34,45,66)

print(s1.avg())
print(s1.get_m1())


#2) Class method : It is used for working with class variable

#Syantax : @classmethod
#          def Function-name (cls):  cls indicate class
#               statement(return cls.class-variable)

#Eg-
class Student:
    school = "telusko"
    @classmethod
    def info(cls):
        return cls.school
print(Student.info())


#3) Static method : This method is not related to any class or object mostly used for non-relatedable fuction

#Syantax : @staticmethod
#          def function-name():  there is nothing inside the bracket indicate static function
#             statement(print("this is static method")

#Eg)
class Student:
    @staticmethod
    def getschool( ):
        print("This is static function")

Student.getschool()


