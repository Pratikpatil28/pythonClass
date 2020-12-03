#OPERATOR OVERLOADING

#BACKENED OPERATION - EVERYTHING OPERATIONS HAPPENING IN PYTHON IS DONE BY METHOD / OBJECT

a= 5             # Backened operations
b = 6
print (a+b)
print(int.__add__(a,b))     #<-- this object is called when you specify add in operations

c = '5'
d = '6'
print(c+d)
print(str.__add__(c,d))      #<-- this object is called for string operation in backened

#Operating Overload

class student:
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):   #we overloaded the operator
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = student (m1,m2)
        return s3
    def __gt__(self, other):
        r1 = self.m1 + self.m2
        r2 = other.m1 + other.m2
        if r1 > r2:
            return True
        else:
            return False

    def __str__(self):
        return '{} {}'.format(self.m1,self.m2)

s1 = student(58,69)
s2 = student(69,65)

s3 = s1 + s2

if s1 > s2:
    print("s1 wins")
else:
    print("s2 wins")

a = 9
print(a.__str__())

print(s1)
print(s2)
print(s3)





