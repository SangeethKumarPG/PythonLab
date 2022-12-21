#!/usr/bin/env python3
def order(x):
    n = 0
    while(x!=0):
        n = n + 1
        x = x // 10

    return n
def power(x,y):
    if(y == 0):
        return 1
    if y % 2 == 0:
        return power(x,y//2) * power(x,y//2)
    return x * power(x,y//2) * power(x,y//2)
def isAmstrong(n):
    copyOfN = n
    d = 0
    s = 0
    k = order(n)
    while n > 0:
        d = n % 10
        s = s + power(d,k)
        n = n // 10
    if s == copyOfN:
        return "Amstrong"

    return "Not Amstrong"
 
n = int(input("Enter a number"))
result = isAmstrong(n)
if result == "Amstrong":
    print("The number is amstrong")
else:
    print("The number is not amstrong")


        
