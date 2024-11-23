# 6)write a python program which will find number of lines ,numbers of words and number of characters in a file.
import os
path="C:\\Users\\Refurbished Lappify\\Downloads\\text-data\\random-data.txt"

try:
    with open(path,"r") as file:
        dlst = file.readlines()
        numl=len(dlst)
        numw=0
        numc=0
        for d in dlst:
            numw+=len(d.split())
            numc+=len(d)
        else:
            print(f"Number of line in {os.path.basename(path)} : {numl}")    
            print(f"Number of word in {os.path.basename(path)} : {numw}")    
            print(f"Number of char in {os.path.basename(path)} : {numc}")    
except FileNotFoundError:
    print("File doesn't Exit")   
except PermissionError:
    print("You don't have sufficient purmission to perform operation") 
except Exception as e:
    print(f"Error due to: {e}")        