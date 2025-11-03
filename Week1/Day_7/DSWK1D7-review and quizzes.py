#challenge 1
name=input("Your name: ")
age=input("Your age: ")
a= int(age)
print(f"Hello {name}!.Next year you'll be {a+1} years old")

#challenge 2
temp=int(input("Hey! What's the temperatre over there?\n"))

if temp >=30:
    print("It's a hot day!")
elif (temp>=20) and (temp <=29) :
    print("The weather is nice.")
else:
    print("It's a bit cold today.")

#challenge 3
items={
    "Bread":1500,
    "Milk": 900,
    "Eggs":2000,
}
total=sum(items.values())

for key,value in items.items():
    print(f"{key} : {value}")
print(f"Total ={total}")