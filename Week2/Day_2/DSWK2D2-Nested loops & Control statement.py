for i in  range(1,10):
    if i==5:
        break       #this allows the code to break when it is about getting to 5.
    print(i)       #So the code prints all number before 5 and end at 4.
print("Done✅")

    #Example 2
for i in  range(1,11):
    if i==5:
        continue        #The continue data type allows you to skip the value 5 and move on from there reaching 10
    print(i) 
print("Completed👌")  

#NESTED LOOP
flavours=["Vanilla","Strawberry","Chocolate"]
toppings=["Hot fudge","Oreos","Sprinkles"]

for one in flavours:
    for two in toppings:
        print(one,"topped with",two)