#Special variable __init__

#It works  approx like Constructor

#Its just like __name__ special variable

class computer:
    def __init__(self):

        print('in init')

    def config(self):
        print("Pratik macbooks")

com1=computer()
com2=computer()


com1.config()
com2.config()

#It runs as many times as the object is called

class computer:
    def __init__(self,cpu,ram ):
        self.central =cpu
        self.memory= ram

    def config(self):
        print("config is", self.memory,self.central)

com1=computer('i5',16)

com2=computer('ryzen 5',16)

com1.config()
com2.config()


#self is related to object(com1,com2) so it is taken automatically

