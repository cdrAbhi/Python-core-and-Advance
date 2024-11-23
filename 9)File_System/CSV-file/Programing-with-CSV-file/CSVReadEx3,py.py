#program for Reading the Data from CSV Files---by using csv module
#CSVReadEx2,py----csv.reader()
import csv
with open("E:\\KVR-PYTHON-9AM\\FILES\\NOTES\\BOOKS.csv","r") as fp:
    csvr=csv.reader(fp) # Here csvr is an object of <class , csv.reader>
    for record in csvr: # record is an object of <class,list>
       for value in record:
           print("{}".format(value),end="\t")
       print()


