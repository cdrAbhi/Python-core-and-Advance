#Program for creating CSV File by using CSV module
#CSVDictWriterEx1.py
import csv
colnames=["BID","BNAME","PRICE","PUBLISHER"]
records=[{"BID":111,"BNAME":"PYTHON","PRICE":566,"PUBLISHER":"TATAMCGRAH"},
            {"BID":222,"BNAME":"C++","PRICE":366,"PUBLISHER":"KINLEY"},
           {"BID":333,"BNAME":"C","PRICE":216,"PUBLISHER":"PEARSON"},
        {"BID":444,"BNAME":"DJANGO","PRICE":465,"PUBLISHER":"PSF"},
    {"BID":555,"BNAME":"HTML","PRICE":166,"PUBLISHER":"HIMALAYA"}] # Dicts of list
with open("E:\\KVR-PYTHON-9AM\\FILES\\NOTES\\BOOKS.csv","w") as fp:
    csvdwr=csv.DictWriter(fp,fieldnames=colnames)
    csvdwr.writeheader()
    csvdwr.writerows(records)
    print("CSV File created with Dict Objects--Verify")



