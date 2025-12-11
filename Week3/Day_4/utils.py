#Creating utility libary
import csv
def add(a,b):
    return a+b
def substract(a,b):
    return a-b
def greet_user(name):
    return f"Hello {name}, Welcome back!"
def total_column(csv_file, column_name):
    total=0
    with open(csv_file, "r") as f:
        rd=csv.DictReader(f)
        for row in rd:
            #removing commas and currencies.
            value=row[column_name].replace(",", "").replace("$","")
            total+=float(value)
        return(total)