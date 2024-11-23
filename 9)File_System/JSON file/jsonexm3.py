#Program for Demonstrating JSON File
import json
try:
with open("student.json","w") as fp:
    jd=json.loads(d1,fp)
    for k in d:
        print(f"{k}==>{d[k]}")
except FileNotFoundError:  
    print("File doesn't Exit")