#Inheritance

#Types of inheritance
#1)Single inheritance - Defines single class connected

class A:  #Eg
    def f1(self):
        print("1.self")

class B(A):
    def f2 (self):
        print("2.self")

b = B ()
b.f2()
b.f1()


#2) Multi inheritance - Defines a row of inheritance

class C: #Eg
    def f3(self):
        print(3)

class D(C):
    def f4(self):
        print(4)

class E(D):
    def f5(self):
        print(5)

e = E()
e.f3()
e.f4()
e.f5()

#3) Multiple level inheritance

class I(A):
    def a1(self ):
        print(1)
class J:
    def a2(self):
        print(2)

class L(I,J):
    def a3(self ):
        print(3)

l = L()
l.f1()
l.a1()
l.a2()
l.a3()


