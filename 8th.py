#Type of arguments
def person(name,age):#Formal Arguments
    print(name)
    print(age)
person('Pratik',18)# Actual arguments

#a) Postion Arguments
def person(name,age):
    print(name)
    print(age)
person('Pratik',18)#Postion Arguments

#b) Keyword Arguments
def person(name,Age):
    print(name)
    print(Age)
person(Age=18,name='Pratik')#keyword arguments

#c) Default Agruments
def person(name,age=18):#[age=18]= default arguments
    print(name)
    print(age)
person('Pratik')

#d) Variable Lenght
def sum(a,*b):
    print(a)
    print(b)
    c=a
    for i in b:
        c=c+1
    print(c)
sum(5,6,11,8)

#e) Keyword variable Lenght Arguments
def person(name,**data):# If you use Single Staer[*data] it will give error
    print(name)
    print(data)
person('Pratik', city='Pune', age=18)

###########OR##########In this arguments to write in another way

def person(name,**data):
    print(name)
    for i,j in data.items():
        print(i,j)
person("Pratik",age=18, City='Pune')
