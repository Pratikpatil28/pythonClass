#Anonymous Function AkA lambda

i = lambda a: a*a
result = i(5)
print (result)

#lambda can be used with
#1 Filter | 2 Map | 3 Reduce
print("#1 Filter ")
#1 Filter Eg:
nums = [1,3,2,4,6,5,7]
even = list(filter(lambda n:n%2==0,nums))
print(even)

#2 Map Eg
print("#2 Map")
doubles = list(map(lambda n:n*2,even))
print(doubles)

#3 Reduce Eg
print('#3 Reduce')
from functools import reduce
sum = reduce(lambda a,b:a+b, doubles)
print(sum)