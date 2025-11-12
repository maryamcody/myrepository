#creating a new file
#newfile =open("New file","x")
#newfile.close()

import os
print("Checking if the file exists or not")
if os.path.exists("New file"):
    os.remove("New file")
else :
    print("file does not exist")
os.rmdir("my folder")


