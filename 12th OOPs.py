#Iterator

#It works as loop but gives out result one by one

class Topten:

    def __init__(self):
        self.num = int(input("Enter the value"))

    def __iter__(self):
        return self

    def __next__(self):
        
        if self.num <= 10+e:

            val = self.num

            self.num += 1

            return val
        else:
            raise StopIteration

values = Topten()
for i in values:
    print(i)