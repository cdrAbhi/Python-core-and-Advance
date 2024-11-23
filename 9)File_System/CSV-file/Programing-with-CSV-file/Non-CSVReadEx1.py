#program for Reading the Data from CSV Files---by using File Pointer which is an object TextIOWrapper
#Non-CSVReadEx1.py
with open("E:\\KVR-PYTHON-9AM\\FILES\\NOTES\\student.csv","r") as fp:
    csvfiledata=fp.read()
    print(csvfiledata)