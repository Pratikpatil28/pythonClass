# Constructor,self & Comparing Objects

# We are going to see that why __init__ is actually a constructor
# what is self actually & its work
#How to compare objects


#1) Objet Address
#class computer:
#    pass

#c1 = computer()   #Every time you createan object
#c2 = computer()   # it is allocated to new space/address


#print(id(c1))
#print(id(c2))


# How the size of object declared
#Depends on the number of variables & size of each variable


# who allocates size to object
# constructor
#Eg- c1= [computer()] --> This is constructor as the init method will be called internally

#2) What is self
# How to update value independtly of object

class computer:
    def __init__(self):
        self.name = 'Pratik'
        self.age = 18

   # def update(self):
    #    self.age=19

    def compare(self, other):  # other is not a synatax it just a variable
        if self.age == other.age:
            return True
        else:
            return False
c1=computer()
c1.age=20

c2=computer()

if c1.compare(c2):
    print("They are same")
else:
    print("They are different")



print(c1.name)
print(c2.name)











