import os

# Creates a file for expenses if non existant
file_path = "expenses_project.txt"
open(file_path, 'a', encoding='utf-8').close()

current_expenses = {}

# Function for this specific input
def cont():
    input("\nPress Enter to continue...")

# Function to act as clear terminal
def clear():
    os.system("cls" if os.name == "nt" else "clear")
    print()

# Check for Comma Function (Extra commas mess up data extraction from file)
def check_commas(prompt):
    while True:
        value = input(prompt)
        if "," in value:
            print("Commas are not allowed. Please try again.")
        else:
            return value.strip()


# Function to add expenses
def add_expense():
    global current_expenses

    clear()
    while True:
        try:
            amount = float(input("Enter price for expense: "))
            break
        except ValueError:
            print("Please enter a valid number.")

    category = check_commas("Enter category for expense: ")
    name = check_commas("Enter name for expense (Make sure each name is unique): ")
    date = check_commas("Enter date for expense: ")


    lower_name = name.lower()
    if lower_name in current_expenses:
        print("Existing expense found - updating it.")
    else:
        print("New expense added.")

    current_expenses[lower_name] = [amount, category, date]
    cont()


# Function to Delete Expense
def del_expense():
    global current_expenses

    del_name = input("Enter name of desired expense: ").lower()

    if del_name in current_expenses:
        del current_expenses[del_name]
        print(f"{del_name} deleted successfully.")
    else:
        print(f"{del_name} not found in expenses.")
    
    cont()


# Search function
def search():
    clear()

    query = input("Enter name of desired expense: ")
    lower_query = query.lower()
    
    if lower_query in current_expenses:
        print(current_expenses[lower_query])
    else:
        print(query + " was not found in your expenses - Make sure name is correctly inputted")

# Function to view expenses 
def view_expense():
    while True:
        search()
        cont()

        search_continue = input("Type 1 to continue searching, enter to quit search: ")
        if search_continue != "1":
            break

# Function to view a summary
def view_summary():
    global current_expenses
    clear()

    if not current_expenses:
        print("No expenses recorded yet.")
        cont()
        return

    # Print header
    print(f"{'Name':<20} {'Amount':>10} {'Category':<15} {'Date':<12}")
    print("-" * 60)

    # Print each expense in a row
    for name, data in current_expenses.items():
        amount, category, date = data
        print(f"{name:<20} {amount:>10.2f} {category:<15} {date:<12}")

    print("-" * 60)
    print(f"Total Expenses: {sum(data[0] for data in current_expenses.values()):.2f}")
    
    cont()

# Save Expenses to File
def save_expenses():
    with open(file_path, "w", encoding="utf-8") as file:
        file.write("name,amount,category,date\n")  # header

        for name, data in current_expenses.items():
            amount, category, date = data
            file.write(f"{name},{amount},{category},{date}\n")

# Load Expenses from File
def load_expenses():
    global current_expenses
    current_expenses = {}

    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()

    for line in lines[1:]:
        line = line.strip()
        if not line:
            continue

        name, amount, category, date = line.strip().split(",", 3)
        current_expenses[name.lower()] = [float(amount), category, date]

load_expenses()

# Main loop
while True:
    clear()

    print("1. Add Expense \n2. Delete Expense \n3. View Expense \n4. View Summary \n5. Exit")
    print("-------------------------------------------------------------------")
    print("Enter Corresponding Number for Task Below - Any other input to exit")
    choice = input("")

    if choice == "1":
        add_expense()
    elif choice == "2":
        del_expense()
    elif choice == "3":
        view_expense()
    elif choice == "4":
        view_summary()
    else:
        save_expenses()
        clear()
        print("Program Complete")
        break