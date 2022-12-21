#!/usr/bin/env python3
list = []
print("Enter the number of elements to be in an array")
n = int(input())
print("Enter the elements to the list")
for i in range(0,n):
    k = int(input("Enter the "+str(i)+"th element to the list "))
    list.insert(i,k)

print(list)
print("Size of list is",len(list))
list.sort()
print("Sorted List",list)
list.sort(reverse=True)
print("Third Largest element is ",list[2])
#length_of_list = list.len



