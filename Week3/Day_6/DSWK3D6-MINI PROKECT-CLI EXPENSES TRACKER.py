# MINI PROJECT - CLI EXPENSE TRACKER
# This program allows the user to add expenses, view them, and calculate the total amount spent.
# Data is stored in a CSV file called CLIExpenses.csv.
import csv           # To handle CSV file reading and writing
import os            # To check if the CSV file exists
from datetime import datetime  # To handle dates and timestamps

CSV_FILE ="CLIExpenses.csv"     # Name of the CSV file to store expenses


# Function to add a new expense
def add_expense():
    # Prompt user to input expense details
    Category = input("Category: ")
    Amount = input("Amount: ")
    Description = input("Description: ")
    
    # Get current date and time in a readable format
    Date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Check if the CSV file already exists
    # This is to ensure that the header row is written only once
    file_exists = os.path.isfile(CSV_FILE)
    
    # Open the CSV file in append mode to add new expense
    with open(CSV_FILE, "a", newline="") as f:
        writer = csv.writer(f)

         # If file does not exist, write the header row first
        if not file_exists:
            writer.writerow(["Date", "Category", "Amount", "Description"])
            # Write the expense data as a new row in the CSV file
        writer.writerow([Date, Category, Amount, Description])
        print("Expense added successfully.\n")

# Function to view all expenses
def view_expense():
    try:
        # Open CSV file in read mode
        with open(CSV_FILE, "r") as f:
            reader = csv.reader(f)

            next(reader, None)
            print("\n_EXPENSES_")
            # Iterate through each expense row and print formatted details
            for row in reader:
                print(f"Date: {row[0]}, Category: {row[1]}, Amount: {row[2]}, Desc: {row[3]}\n")
    except FileNotFoundError:
        # Handle case where CSV file does not exist yet
        print("No expenses found.\n")

# Function to calculate total expenses
def calculate_total():
    total = 0   # Initialize total
    try:
         # Open CSV file in read mod
        with open(CSV_FILE, "r") as f:
            reader = csv.reader(f)
            next(reader, None)

            # Iterate through each row to sum amounts
            for row in reader:
                try:
                    value = row[2].replace(",", "").replace("$", "")     # Remove commas or currency symbols and convert to float
                    total += float(value)
                except ValueError:
                    # Handle invalid numeric values gracefully
                    print(f"Skipping invalid amount: {row[2]}")
    except FileNotFoundError:
         # Handle case where CSV file does not exist
        print("No expenses found.\n")
        return
    
      # Print the total amount of expenses
    print(f"\nTotal expenses: {total}\n")

# Main function to provide a command-line interface for the user
def main():
    while True:      # Infinite loop until user chooses to exit
        # Display menu options
        print("1. Add Expenses")
        print("2. View Expenses")
        print("3. View Total")
        print("4. Exit")

         # Get user's menu choice
        choice = input("Choose an Option: ")

         # Call the corresponding function based on user input
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expense()
        elif choice == "3":
            calculate_total()
        elif choice == "4":
            print("Goodbye!")   # Exit message
            break      # Exit the loop and program
        else:
            print("Invalid choice.\n")   # Handle invalid input

# This ensures that main() runs only if this script is executed directly
# It will not run if this file is imported as a module elsewhere
if __name__ == "__main__":
    main()
