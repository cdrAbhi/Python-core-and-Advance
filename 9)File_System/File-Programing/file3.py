# 3)write a python program which will display content of any file name (use read and readlines)        
path="C:\\Users\\Refurbished Lappify\\Downloads\\text-data\\student.txt"

try:
    with open(path,"r") as file:
        # lst=file.readlines()
        # print(lst)
        s=file.read()
        print("string data = {}".format(s))
except FileNotFoundError:
    print("File doesn't Exit")     
except PermissionError:
    print("== Please Enter file_name along with directory path ==")       