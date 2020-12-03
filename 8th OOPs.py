# Introduction to Polymorphism

# 1) DUCK TYPING
# 2) OPERATING OVERLOADING
# 3) METHOD OVERLOADING
# 4) METHOD OVERRIDING

# DUCK TYPING - IT SEEMS LIKE A COPY, EG- IF A BIRD SWIMS LIKE A DUCK, QUACK LIKE A DUCK ITS A DUCK

class Laptop:
    def code(self, ide):
        ide.execute()


class Pycharm:
    def execute(self):
        print("Compiling")
        print("Running")


class Myedi:
    def execute(self):
        print("Spelling check")
        print("All error solved")


ide = Myedi()

lap1 = Laptop()
lap1.code(ide)
