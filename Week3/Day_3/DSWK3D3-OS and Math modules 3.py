#PRACTICE
import os
import math
import csv

# Listing out files
folder="MyFolder"
files=os.listdir(folder)
print(files)

#Read CSV
with open(os.path.join(folder, "numbers.csv"), "r") as f:
    reader=csv.reader(f)
    for row in reader:
        for num in row:
            value=int(num)
            print("value: ", value)
            print("Square root: ",math.sqrt(float(value)))
            print("Factorial: ", math.factorial(value))