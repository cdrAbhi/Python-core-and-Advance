#Program for Reading the records from File by using Un-pickling Process
#EmpUnPickEx1.py
import pickle
def reademprecords():
    with open("E:\\KVR-PYTHON-9AM\\FILES\\employee.data","rb") as fp:
        print("--------------------------------------------------------")
        while(True):
            try:
                emprec = pickle.load(fp) # Here emprec is an object of list
                for val in emprec:  # [100, 'RS', 1.1, 'Author']
                    print("{}".format(val),end="\t")
                print()
            except EOFError:
                print("--------------------------------------------------------")
                break
#main program
reademprecords()