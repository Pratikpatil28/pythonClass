#Decorators
#It adds extra features to pre-exsiting function by not changing it

def div(a,b):
    print(a/b)
def smart_div(func):
    def inner(a,b):
        if a<b:
            a,b=b,a
        return func(a,b)
    return inner
div = smart_div(div)
x=int(input("Enter the value of x="))
y=int(input("Enter the value of y="))
div(x,y)
