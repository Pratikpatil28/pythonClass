class Try:
    def __init__(self,name,age  ):
        self.name=name
        self.age=age

    def update(self ):
        self.age = 30

    def compare (self,other):

        if self.age==other.age:
            return True
        else:
            return False
    def print(self):
        print(self.name,self.age)

c1=Try("pratik",18)
c2= Try("Monu",10)

if c1.compare(c2):
    print("Same age")
else:
    print("Different age")

c1.print()
c2.print()

