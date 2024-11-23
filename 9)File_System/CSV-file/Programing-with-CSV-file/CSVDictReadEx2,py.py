#program for Reading the Data from CSV Files---by using csv module in the form of Dict
#CSVDictReadEx2,py----csv.DictReader()
import csv
with open("E:\\KVR-PYTHON-9AM\\FILES\\NOTES\\books.csv","r") as fp:
    csvdr=csv.DictReader(fp) # here csvdr is an object of <class, csv.DictReader>
    i=1
    for record in csvdr: # Here record is an object of <class, dict>
        print("\t\t{} Book Record".format(i))
        print("-" * 50)
        for k,v in record.items():
            print("\t{}--->{}".format(k,v))
        print("-"*50)
        i=i+1

