#Program for Reading the records from File by using Un-pickling Process
#EmpUnPickEx2.py
import pickle
path="C:\\Users\\Refurbished Lappify\\Downloads\\text-data\\image.png"
def reademprecords():
    with open(path,"rb") as fp:
        print("--------------------------------------------------------")
        while(True):
            try:
                emprec = pickle.load(fp) # Here emprec is an object of list
                print("{}\t{}".format(emprec[0],emprec[1]),end="")
                print()
            except EOFError:
                print("--------------------------------------------------------")
                break
#main program
reademprecords()