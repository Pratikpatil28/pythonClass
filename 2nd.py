from numpy import *
a= array([1,2,3,4])
b=a.copy()
a[2]=2
print(a)
print(b)
print (id(a))
print (id(b))