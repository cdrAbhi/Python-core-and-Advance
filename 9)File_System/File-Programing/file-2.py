# 2)write a python program which will accept any type of data and write to the file and save to file until we press @ symbol

path="C:\\Users\\Refurbished Lappify\\Downloads\\text-data\\student.txt"

with open(path,"a+") as file:
    try :
        while True:
            option=input("Do you want to enter data(yes/no): ")
            if not option.isalpha():
                print("Invalid Option")
            elif option.lower()=="no":
                # print(file.read()) 
                break
            elif option.lower()=="yes":
                d=input("Enter data : ")
                file.write(d+"\n")
            else:
                print("Invailid Option")
        print("*"*30)
        print("=== Data save Successfully ===")  
        print("*"*30)            
    except PermissionError:
        print("You don't have write Permission")        
        

while True:
    o=input("You want to read file data(yes/no) : ")  
    if not o.isalpha():
        print("Invalid Option")
    elif(o.lower()=="yes"):
        print("*"*30)
        with open(path,"r") as file :
            print(file.read()) 
            print("==== Thank you Come Again ====")  
    elif(o.lower()=="no"):     
        break
    else:
        print("Invalid Option : {}".format(o))   
        