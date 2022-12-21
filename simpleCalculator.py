#!/usr/bin/env python3
def addition(a,b):
    return a+b

def subtraction(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

a= int(input("Enter a number"))
b = int(input("Enter the second number"))
print("Enter the options")
print("Enter 1 for addition")
print("Enter 2 for subtraction")
print("Enter 3 for multiplication")
print("Enter 4 for division")
print()
option = int(input("Enter your choice"))
if option == 1:
    c=addition(a,b)
    print("Sum is",c)
elif option == 2:
    c=subtraction(a,b)
    print("Difference is",c)
elif option == 3:
    c=mul(a,b)
    print("Product is",c)
elif option == 4:
    c=div(a,b)
    print("Divsion = ",c)
else:
    print("Enter a valid option")


