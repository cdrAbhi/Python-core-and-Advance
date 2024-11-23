#POrogram for removing the file name
#RemoveFileName.py
import os
try:
    os.remove("main.py")
    print("File Removed--verify")
except FileNotFoundError:
    print("File does not exist")