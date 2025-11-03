#accepting inputs
shopping=["bread", "butter", "milk", "egg",  "sugar"]
print ("ORIGINAL SHOPPING LIST: ",shopping)

print("PLEASE ENTER YOUR 5 ITEMS IN THE SHOPPING LIST\n")
A=input("ENTER ITEM 1\n")
X=input("ENTER ITEM 2\n")
C=input("ENTER ITEM 3\n")
B=input("ENTER ITEM 4\n")
G=input("ENTER ITEM 5\n")
new_shopping= shopping+[A, X, C, B, G]

print (f"your shopping list are :{new_shopping} and the total number is {len(new_shopping)}")
print(new_shopping[-1])

new_shopping_tuple= tuple(new_shopping)
print ("tuple version :", new_shopping_tuple)
new_shopping_tuple.append("car")

