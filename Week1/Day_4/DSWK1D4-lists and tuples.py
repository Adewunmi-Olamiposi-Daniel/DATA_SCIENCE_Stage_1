#LIST
shopping_list=["bread", "butter", "milk", "egg"]
print (shopping_list)

#accessing and slicing
print(shopping_list[0])
print(shopping_list[-1])
print(shopping_list[0:2])
print(shopping_list[-2:])
print(shopping_list[:2])
print(shopping_list[1]+" and "+ shopping_list[3])

#mutating
shopping_list[1]="no fat butter"  #changes "butter" to "no fat butter"
print (shopping_list)
shopping_list.append("sugar")     #add "sugar" to the list
print (shopping_list)
shopping_list.remove("milk")      #removes "milk" from the list
print (shopping_list)

#TUPLES
coordinates=(6.4,3.2)
print (coordinates)
print (coordinates[0])