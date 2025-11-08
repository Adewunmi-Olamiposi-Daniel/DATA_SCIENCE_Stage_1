#error handling challenge
try:
    x=int(input("Enter a value for numerator: "))
    y=int(input("Enter a value for denominator: "))
    print(x/y)
except ValueError:
    print("Enter a correct value")
    print("Program unsuccessful")
except ZeroDivisionError:
    print("You can not input the value 0.Try again.")
    print("Program unsuccessful")
else:
    print("Your equation have been completed")
    print("Program successful")

#challenge 2
Stock_items=["Real Estate", "Oil & Gas",'Agriculture']
try:
    index=int(input("Enter an index (range 0-2): "))
    print(f"The stock in this positions is: {Stock_items[index]}")
except ValueError:
    print("Enter numbers only")
except IndexError:
    print("That position does not exist")

#challenge 3
while True:
    try:
        ans=float(input("What is 5% of the Facebook valuated?").strip())
        if ans==69.6:
            print("$69.6 Billion.")
            print("Correct! You got your analysis right.")
            break
        else:
            print("Wrong! Do more work on the assignment.")
    except ValueError:
        print("Numbers only.")