#Program for  adding new record to CSV File to the existing CSV File
#CSVWriterEx2.py----csv.writer()
import csv
rec=[900,"Suraj",13.12,"HR"]
with open("E:\\KVR-PYTHON-9AM\\FILES\\NOTES\\employee.csv","a") as fp:
    csvwr=csv.writer(fp)
    csvwr.writerow(rec)
    print("New Record Added to CSV File--Verify")

