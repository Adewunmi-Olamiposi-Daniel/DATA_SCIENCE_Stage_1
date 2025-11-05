#CHALLENGE 1
for i in range (1,6):
    for j in range(1,6):
        print(i*j, end=" ")
    print()

#CHALLENGE 2
for o in range (1,11):
    if o %2!=0:
        continue
    print(o)

#CHALLENGE 3
Passw = "D@t@_is_great"
attempt = 0
maxAttempt = 3

while attempt < maxAttempt:
    p = input("Enter your Password: ")
    if p == Passw:
        print("Access Granted✅")
        break
    else:
        attempt += 1
        remainder = maxAttempt - attempt
        if remainder > 0:
            print(f"Incorrect Password! Try again. You have {remainder} trials left")
        else:
            print("Account Locked❌")
