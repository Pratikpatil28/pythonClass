"""
Binary search in python

Logic :
  In binary there are 3 terms
  1) Lower Bound  2)Mid  3)Upper Bound

  Eg - array = [1,3,5,6,7]
  Here 1 = lower Bound  7 = Upper Bound
        Mid = lower+Upper / 2   (mid calculated in index value)
        eg here like - 0[l] + 4[U] / 2
          Mid = 2--> value is 5
          Therefore mid value will be 5
  Condition of change mid :
    If the SEARCH VALUE is SMALLER then,
    change UPPER BOUND & MID becomes the new UPPER BOUND
    If the SEARCH VALUE is BIGGER then,
    change LOWER BOUND & MID becomes the new LOWER BOUND

"""


#Eg - While Loop
pos = -1

def search(list, n):

    l = 0
    u = len(list)-1

    while l <= u:
        mid = (l+u) // 2

        if list[mid] == n:
            globals()['pos'] = mid
            return True
        else:
            if list[mid] < n:
                l = mid+1
            else:
                u = mid-1

    return False


list = [4,7,8,10,12,45,99,102,702,10987,56666]
n = 56666

if search(list, n):
    print("Found at ",pos+1)
else:
    print("Not Found")




#Eg - For Loop
pos = -1

def search(ar,a):
    s=0
    e=len(ar)-1
    for i in range(s,e+1):
        mid = s + (e-s) // 2
        if ar[i] == a:
            globals()['pos'] = a
            return True
        else:
            if ar[mid] < a:
                s = mid+1
            else:
                e = mid-1

    return False

ar = [1,3,4,6,7,8]



a = 8

if search(ar,a):
    print("Found",pos)
else:
    print("Not Found")
    

