#Factorial

def fact(n):
    f=1
    x=n
    for i in range (1,n+1):
        f=f*i
        print("Sequence of factorial ",f)

    return f
x=int(input("Enter the value"))

result = fact(x)
print("Factorial of ",x,"is ",result)