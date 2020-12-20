import os

directory_name = input("What directory would you like to save your file? ")
file_name = input("What is the name of the file you want to save to the " + directory_name + " directory? ")

completePath = directory_name + file_name
path = os.path.join(directory_name,file_name)

try:
    os.path.isfile(path) #check if file exists
    with open(completePath, 'a') as fileHandle:
        input = input("Please enter your name, address, and phone number: ")
        fileHandle.write("\n" +input)
except FileExistsError:
    os.mkdir(directory_name) #adds directory
    with open(completePath, 'w') as fileHandle:
        input = input("Please enter your name, address, and phone number: ")
        fileHandle.write("\n" + input)

with open(completePath, 'r') as file_Handle: 
    for line in file_Handle:
        print(line, end='')

