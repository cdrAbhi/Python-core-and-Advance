# 5)write a python program which will copy an image from one file to another file
import os
import webbrowser

spath="C:\\Users\\Refurbished Lappify\\Downloads\\All-image\\knights_tour_2.png"
dpath="C:\\Users\\Refurbished Lappify\\Downloads\\text-data\\\\image.png"

# try:
#    with open(spath,"rb") as imag:
#        d=imag.read()
#        with open(dpath,"wb") as img:
#            img.write(d)
#            print("image {} Copy to {} succesfully".format(os.path.basename(spath),os.path.basename(dpath)))
# except FileNotFoundError:
#     print("File Does'nt exit")
# except PermissionError:
#     print("You don't have permssion for current operation") 
# except Exception as e:
#     print(f"Error due to: {e}")       


# Mth-1  : To openfile

# while True:
#     o = input("You want to read file data (yes/no): ")
#     if not o.isalpha():
#         print("Invalid Option")
#     elif o.lower() == "yes":
#         print("*" * 30)
#         os.startfile(dpath)  # This will open the image using the default image viewer
#         print("==== Thank you for using this program. Come Again ====")
#     elif o.lower() == "no":
#         print("==== Thank you for using this program. Come Again ====")
#         break
#     else:
#         print("Invalid Option: {}".format(o))



# Mth-2  : To openfile


while True:
    o = input("Do you want to open Image (yes/no): ")
    if not o.isalpha():
        print("Invalid Option")
    elif o.lower() == "yes":
        print("*" * 30)
        webbrowser.open(dpath)  # This will open the image in the default web browser
        print("==== Thank you for using this program. Come Again ====")
        break
    elif o.lower() == "no":
        print("==== Thank you for using this program. Come Again ====")
        break
    else:
        print("Invalid Option: {}".format(o))
