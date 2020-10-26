#Pass list to a function


def count(lst):
    even=0
    odd=0
    for i in lst:
        if i%2==0:
            even+=1
        else:
            odd+=1
    return even,odd
lst=[20,23,14,19,26,24,28,47,16]
even,odd = count(lst)

print("Even={} and Odd={}".format(even,odd))


