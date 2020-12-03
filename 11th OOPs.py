#Abstract class & abstract method

#Python doesn't officaly support abstarct method so we use a module ABC to use abstract method
#ABC - ABSTRACT BASE CLASS

from abc import ABC, abstractmethod
class Computer(ABC):
    @abstractmethod
    def process(self):
        pass

class Laptop(Computer):
    def process(self):
        print("First time")

class Desktop(ABC):
    @abstractmethod
    def show(self):
        pass

class Mac(Desktop):
    def show(self):
        pass

    def shows(self):
        print("get me value")


class Lap(Mac):
    def show(self):
        print("Get me value")




a1 = Laptop()
a1.process()

a3 = Lap()
a3.shows()
a3.show()