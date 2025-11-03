#challenge 3
n=int(input("Enter a number: "))
for r in range (13,0,-1):
    print(f"{n} x {r} = {n*r}")

#challenge 4
correctPassw= "Data_is_life123"
attempt=""

while attempt!=correctPassw:
    attempt=input("Enter your Password: ")
    if attempt!=correctPassw:
        print("Incorrect Password!Try again")
print("Access Granted✅")