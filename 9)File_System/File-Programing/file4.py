# 4)write a python program which will copy the content of one file into another file
import os
spath="C:\\Users\\Refurbished Lappify\\Downloads\\text-data\\student.txt"
dpath="C:\\Users\\Refurbished Lappify\\Downloads\\text-data\\studentcopy.txt"

try:
    with open(spath,"r") as file:
        data=file.read()
        with open(dpath,"a") as cfile:
            cfile.write(data)
            print("====Data copy from file {} to {}=====".format(os.path.basename(spath),os.path.basename(dpath)))
except FileNotFoundError:
    print("File or path or directory doesn't exit")     
except PermissionError:
    print("You haven't permission to perform task on path : {}".format(spath))

while True:
    o=input("You want to read file data(yes/no) : ")  
    if not o.isalpha():
        print("Invalid Option")
    elif(o.lower()=="yes"):
        print("*"*30)
        with open(dpath,"r") as file :
            print(file.read()) 
            print("==== Thank you for using this program Come Again ====")  
    elif(o.lower()=="no"):     
        print("==== Thank you for using this program Come Again ====") 
        break
    else:
        print("Invalid Option : {}".format(o))   
                