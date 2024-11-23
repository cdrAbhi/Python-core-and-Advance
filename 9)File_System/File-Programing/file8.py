# 8)write a python program which will read the content from any file and print the content of the file in reverse order .
import os
dpath="C:\\Users\\Refurbished Lappify\\Downloads\\text-data\\random-data.txt"

try:
    print("*"*50)
    print(f"In Reverse order content of file {os.path.basename(dpath)}")
    print("*"*50)
    with open(dpath,"r") as file :
        dlst=file.readlines()
        for l in dlst:
            print(l[::-1])
        else:
            print("*"*50)    
        print("==== Thank you for using this program Come Again ====\n")   
        
except FileNotFoundError:
    print("File or path or directory doesn't exit")     
except PermissionError:
    print("You haven't permission to perform task on path : {}".format(spath))

