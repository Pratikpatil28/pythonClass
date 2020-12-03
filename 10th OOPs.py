#Method Overloading & Method Overriding

#Method Overloading - If in a class you have 2 methods of same name but different parameters or arguments
                      # is called methods Overloading

#Eg - def student (a,b)
#      def student (a,b,c)

# but this method is not present in python


#Method overriding - If you have 2 methods with same paramenters or arguments in inheritance with different classes
#EG - Class A
#    def student (a,b)
#    Class B
#    def student (a,b,c)

class student:


    def sum (self, a=None, b=None,c=None):

        s = 0
        if a !=None and b!=None and c!=None:
            s=a+b+c
        elif a!=None and b!=None:
            s=a+b
        else:
            s=a
        return s


s1 = student()
print(s1.sum(1,1,1))


#Eg 2:
class A:
    def show(self):
        print("In show A")

class B(A):
    def show(self):
        print("In show B")

#If you delete show function in B class then it will print Class A show function


a1 = B()
a1.show()
