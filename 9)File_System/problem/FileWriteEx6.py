#Program for reading the Data from KBD and write it to the file
#FileWriteEx6.py
with open("E:\\KVR-PYTHON-9AM\\FILES\\NOTES\\hyd.info","a") as fp:
    print("Enter the Information from KBD for writing it to the file")
    while(True):
        data=input()
        if(data=="@"):
            print("\nData Written to the File--Verify")
            break
        else:
            fp.write(data+"\n")



