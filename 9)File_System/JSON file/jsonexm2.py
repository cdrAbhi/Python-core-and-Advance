#Program for Demonstrating JSON File
import json
# Here dl is an object of
d1='{"Name":"Shiva","Staus":"Almighty","location":"Kailash"}'
# we can save dict object data into File by using a predefined function called json.dump("file.json","w")
with open("student.json","w") as fp:
    json.dump(d1,fp)
    print("Json data save to file successfully")