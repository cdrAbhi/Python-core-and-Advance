# 7)write a python program which will get the vowel words only from the given file


import os
path="C:\\Users\\Refurbished Lappify\\Downloads\\text-data\\random-data.txt"

try:
    with open(path,"r") as file:
        dlst = file.readlines()
        print(f"====Vowel word in {os.path.basename(path)} ====")
        for d in dlst:
            nl=list(d.split())
            for w in nl:
                if("a" in w.lower() or "e" in w.lower() or "i" in w.lower() or "o" in w.lower() or "u" in w.lower()):
                    print(f"==> {w}")
        else:
            print("*"*50)
            print("==Operation perform Succesfully==")    
                
except FileNotFoundError:
    print("File doesn't Exit")   
except PermissionError:
    print("You don't have sufficient purmission to perform operation") 
except Exception as e:
    print(f"Error due to: {e}")        