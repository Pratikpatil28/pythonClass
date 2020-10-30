# Part of special variable __name__
#merged with 16thA,speciA
#merged with module speciB
from speciB import add

def fun1():
    add()
    print("This is fun 1", __name__)


def fun2():
    print("This is fun 2")


def main():
    fun1()
    fun2()


main()