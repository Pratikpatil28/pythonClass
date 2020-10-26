#SCOPE TERM
#Has 2 types
# 1. Local variable: Defined in function
# 2. Global variable: defined outside function

#Attempt 1st
a=10 #GLobal
def something():
    a=9 #Local
    print("fun",a)
something()
print("Global",a)


#Attempt 2nd
#if you want to change the global variable by change varibale inside function
a=10
def something():
    global a #Change local to global variable type
    a=9
    print("fun",a)
something()
print("Global",a)


#Attempt 3rd
#We can use global/local variable at same time and without
#affecting local variable we can change the value of global variable
a=10
print('1st',id(a))
b=20
def something():
    a=9
    x=globals()['a']
    print('2nd',id(x))  #Just to confirm
    print('3rd',x)
    print("In Fun 4",a)
    globals()['a']=15
something()
print('5',a)
print('6',b)
