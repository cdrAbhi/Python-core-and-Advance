# 1)write a python program which will accept students detail and write to the file
path="C:\\Users\\Refurbished Lappify\\Downloads\\text-data\\student.txt"
# with open(path, "a") as fr:
#     while True:
#         option = input("Do you want to Enter data(yes/no): )")
#         if option.lower() == "no":
#             break
#         else:
#             name = input("Enter your name :")
#             number = input("Enter your number :")
#             marks = input("Enter your marks :")
#             fr.write(name+"\t")
#             fr.write(number+"\t")
#             fr.write(marks+"\n")


try:
    with open(path, "r") as fr:
        data=fr.readlines()
        # print(data,"\ntype data : {}".format(type(data)))
        print("Student date ")
        print("*"*30)
        for line in data:
            print(line)
        print("*"*30)    
except PermissionError:
    print("Permission Error")