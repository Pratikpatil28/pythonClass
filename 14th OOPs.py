#Exception Handling

#Errors are of two types:
#1] Complie time- The error in syntax as syntactical error
        #Eg - missing common or any syntax error

#2] Logical - Getting a wrong output to given input is called logical error
    #Eg - 2+3 = 4--> Wrong output error

#3] Runtime - A wrong input given by user is called as Runtime error
#Eg] - 6/0 = ZeroDivisionError

# There are two types of statments
#1] Normal Statemnt - Doesnt gove any error
      #eg - a=2 , b=3 , print("Example")
#2] Critical Statement - Can give you error depending on statement / Input
      #Eg - a = 2 , b = 4 , a/b = error

a = 5
b = 0    #This input will create ZeroDivision error
try:   #Built in function
    print("Resource open")
    k = int(input("enter the number"))   #Value error program
    print(k)
    print("Resource open")
    print(a/b)   #Zero division error



except ZeroDivisionError as e:  #ZeroDivsion Error built in
    print("Zero Divsion error","[",e,"]")

except ValueError as e:        #Value error built in
    print("Value input is incorrect","[" ,e , "]")

except Exception as i:        #A general error function
    print("something went wrong")

finally:     #A common ending statement
    print("Resource closed")