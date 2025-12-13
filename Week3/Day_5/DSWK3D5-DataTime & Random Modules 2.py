#Random Modules
import random
print(random.randint(1,100))

#Randomize list
friends=["Ola","Imisi","Ayomide","Eni","Micheal","Samuel"]
print(random.choices(friends))

#Shuffling list
listz=[1,2,3,4,5,6,7,8,9,0]
random.shuffle(listz)
print(listz)

#Rolling the deck(Pratice)
print("WELCOME TO THE TABLE MY FRIEND. LET'S MAKE YOU SOME MONEY.")
for i in range(5):
    Roll_dice=(random.randint(1,6))
    #asking for input.
    pick=int(input("DECK:(1,2,3,4,5,6). Pick:"))

    #conditioning
    if pick==Roll_dice:
       print("WINNER!")
       break
    else:
        print(f"Ouch, Wrong pick. The deck says {Roll_dice}.")
        choice=input("Would you like to double your wager? YES OR NO?\n").lower()
        if choice=="yes" or choice=="y":
            print("Smart Move, my friend")
            print("Next round, baby!")
        elif choice=="no" or choice=="n":
            print("Awwn. Walking away, already.")
            break
        else:
            print("I didn't catch that. I assume that's a yes, then")