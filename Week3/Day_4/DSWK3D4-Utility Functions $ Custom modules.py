#After creatinga utils.py file. I'm accessing it here. COOL
import utils
print(utils.add(10,5))
print(utils.substract(500,230))
print (utils.greet_user("Klaus"))

#Neater way of access
from utils import add,greet_user
print(add(120,65))
print (greet_user("Ola"))

#PRACTICE:
from utils import total_column
total=total_column("Expenses.csv", "Amount")
print("Total Amount: ", total)