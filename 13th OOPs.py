#Generator
# They are same as of Iterator

#Generated by Yield Keyword

def topten():
    n=1
    while n<=10:
        sq = n*n
        yield n
        n+=1
values  = topten()

for i in values:
    print(i)


def prev():   #It controls the iterator as the the value given to yield is max limit and min limit
    yield 1
    yield 2
    yield 3

make = prev()
for e in make:
    print(e)