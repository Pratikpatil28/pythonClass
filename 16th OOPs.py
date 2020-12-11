"""
Linear Search using Python Manully

Search a array using a loop

There will bw 2 Cases sych as:
1] No. Found
2] No. Not Found

"""

# Eg - Using While Loop
pos = 0  # postion index


def search(list, n):  # Defined a function

    i = 0  # Counter in while loop
    while i < len(list):  # While loop
        if list[i] == n:  # IF....ELSE Condition of finding number
            globals()['pos'] = i  # Called global var
            return True
        i += 1  # Incrementer in while loop
    return False


list = [2, 4, 3, 6, 8]  # Array list

n = int(input("Enter the number"))  # Input var

if search(list, n):  # If else condition of print
    print('Found at', pos)
else:
    print('Not found')

# Eg - For loop

pos = -1


def search(ar, a):
    for i in range(len(ar)):
        if ar[i] == a:
            globals()['pos'] = i
            return True
    return False


ar = [5, 8, 4, 6, 9, 2]
a = int(input("Enter the number"))

if search(ar, a):
    print("Found at ", pos)
else:
    print("Not Found")
