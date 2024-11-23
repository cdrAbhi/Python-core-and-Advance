#Program for creating CSV File by using CSV module
#CSVWriterEx1.py----csv.writer()
#Step-1--->Take Header Names Or Col Names
import csv
colnames=["ENO","ENAME","SAL","DSG"]
#Step-2---->Take Records--always in the form of Lists in List
records=[ [1000,"Rossum",56.78,"Author"],
               [2000,"Travis",33.33,"Scientist"],
               [3000,"Kinney",43.33,"Scientist"],
               [4000,"Dennis",53.33,"Developer"],
               [5000,"Startup",13.33,"SE"] ] # Lists of list
#Step-3--Choose the file name and open in write mode
with open("E:\\KVR-PYTHON-9AM\\FILES\\NOTES\\employee.csv","w") as fp:
    csvwr=csv.writer(fp) # here csvwr is an object of <class, csv.Writer>
    #Step-4---Write Header Name
    csvwr.writerow(colnames)
    #Step-5---write Records
    csvwr.writerows(records)
    print("CSV File Created--Verify")



