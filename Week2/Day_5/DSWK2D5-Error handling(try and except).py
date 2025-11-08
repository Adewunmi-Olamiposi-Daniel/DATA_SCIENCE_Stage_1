#error handling (try/except)
try:
    x=int(input("Enter a number: "))
    print(10/x)
except ValueError:
    print("Please enter a valid number.")
except ZeroDivisionError:
    print("You can not divide by zero.")
else:
    print("Operation succesful.")
finally:
    print("Program completed")    