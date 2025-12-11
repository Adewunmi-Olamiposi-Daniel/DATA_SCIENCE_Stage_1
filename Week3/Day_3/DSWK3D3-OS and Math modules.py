#Checking if a folder exists.
import os
if os.path.exists("MyFolder"):
    print("Folder already exists")
    #Creating one if it doesn't.
else:
    print("Creating folder...")
    os.makedirs("MyFolder")

    #Listing all files from a folder
files=os.listdir("DSPYWK1")
print(files)

    #Building file paths(safe across all OS)
Path=os.path.join("MyFolder", "data.csv")
print(Path)