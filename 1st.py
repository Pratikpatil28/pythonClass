from numpy import *
a= array([11,22,33])
b=a.view()
a[1]=7
#This is shallow copy with different address but same array: view

print(b)
print(a)
