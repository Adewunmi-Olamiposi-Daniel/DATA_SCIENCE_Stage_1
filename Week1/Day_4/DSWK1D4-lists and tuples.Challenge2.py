
#accepting 5 inventories
print("Kindly enter 5 inventories")
inventories1=input("enter inventory 1\n")
inventories2=input("enter invenotory 2\n")
inventories3=input("enter invenotory 3\n")
inventories4=input("enter invenotory 4\n")
inventories5=input("enter invenotory 5\n")

management_list=[inventories1, inventories2, inventories3, inventories4, inventories5]

categories_tuple=["Drinks","Snacks", "Toiletries"]

management_list.append("hair gel")
print(management_list)
management_list.remove(inventories5)
print(management_list)

print(f"All available items in stocks are:{management_list} and the total is {len(management_list)}")


new_categories_tuple= tuple(categories_tuple)
print(f"tuple version: {categories_tuple}")
new_categories_tuple.append("Foods")
print(new_categories_tuple)