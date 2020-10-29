# Recursion

#general means a function will call itself like a loop

#How to see recrison limit
#sol-
import sys
print(sys.getrecursionlimit())

#Can we exceed the limit?
import sys
sys.setrecursionlimit(2000)
print(sys.getrecursionlimit())

#Factorial by Recursion
x=int(input("Enter the value"))
def fact(n):
    global x
    x=n
    if n==0:
        return 1

    else:
        return n*fact(n-1)

result= fact(x)

print(result)