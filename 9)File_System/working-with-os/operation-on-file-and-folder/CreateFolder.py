#Program for Creating a Folder at a time
#CreateFolder.py---mkdir()
import os
try:
    os.mkdir("C:\\KVR\\PYTHON")
    print("Folder Created Sucessfully")
except FileExistsError:
    print("Folder alerady exist")
except FileNotFoundError:
    print("Previous  Folder does not Exis")