file = open("myfile.txt","a+")
append_string = "\nthis is a test"
file.write(append_string)
file.close()

file2 = open("myfile.txt","r+")
list_of_contents = file2.readlines()
number_of_lines = 0
for i in list_of_contents:
    print(i)
    number_of_lines +=1

print("Number of lines in file is : ",number_of_lines)