# Two topics

# 1) Constructor in inheritance

# 2) Method Resolution Order ( MRO )

# 1- Constructor in inheritance
# If you create object of subclass it will first try to find init of own class,
# if it is not found then it will call init of SuperClass

class A:
    def __init__(self):
        print("in A init")


class B(A):
    def __init__(self):
        super().__init__()  # This statement calls the init of class A. IF YOU DONT SPECIFIC THIS
                            # IT WILL PRINT ONLY CLASS B INIT..
        print("in B init")


a1 = B()

# Without super class it will only print -[ in B init ]

# 2) Method Resolution Order ( MRO )
# It takes place during multiple - level inheritance
# It order super class to take the left specifed class as super host class
#Eg - class C (A,B) : Class A is on left side to it will take left class as main host

class C:
    def __init__(self):
        print("In C init")

class D:
    def __init__(self):
        print("In D init")

class E(C,D):
    def __init__(self):
        print("In E inti")
        super().__init__()

e = E ()
#Output
# will print C super class as its on its left side specifed by me

class F(C,D):    #There is a way to get left side super class constructor as a print
    def __init__(self):
        print("Next line")
        super(D, self).__init__()   #this method is a built in, if u specify class of
                                    # left side it will print its right side class and it continues

f = F ()
