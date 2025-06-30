import csv
import os

# Global data
expenses = []
budget = 0.0
expenses_file = 'expenses.csv'

# Load expenses from CSV at start
def load_expenses(filename=expenses_file):
    if not os.path.exists(filename):
        return

    try:
        with open(filename, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if all(row[k] for k in ['date', 'category', 'amount', 'description']):
                    try:
                        row['amount'] = float(row['amount'])  # convert string to float
                        expenses.append(row)
                    except ValueError:
                        print("Invalid amount found in CSV. Skipping row.")
        print("Expenses loaded successfully.\n")
    except Exception as e:
        print(f"Error loading expenses: {e}")

# Save expenses to CSV
def save_expenses(filename=expenses_file):
    try:
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=['date', 'category', 'amount', 'description'])
            writer.writeheader()
            writer.writerows(expenses)
        print("Expenses saved successfully.\n")
    except Exception as e:
        print(f"Error saving expenses: {e}")

# Add expense
def add_expense():
    try:
        date = input("Enter date (YYYY-MM-DD): ").strip()
        category = input("Enter category (e.g., Food, Travel): ").strip()
        amount = float(input("Enter amount spent: "))
        description = input("Enter a brief description: ").strip()

        expense = {
            'date': date,
            'category': category,
            'amount': amount,
            'description': description
        }

        expenses.append(expense)
        print("Expense added.\n")
    except ValueError:
        print("Invalid amount. Please enter a number.\n")

# View all expenses
def view_expenses():
    if not expenses:
        print("No expenses found.\n")
        return

    print("\nStored Expenses:")
    for idx, exp in enumerate(expenses, start=1):
        if all(exp.get(field) for field in ['date', 'category', 'amount', 'description']):
            print(f"{idx}. Date: {exp['date']}, Category: {exp['category']}, "
                  f"Amount: ₹{exp['amount']:.2f}, Description: {exp['description']}")
        else:
            print(f"{idx}. Incomplete expense entry – skipped.")
    print()

# Set and track budget
def set_budget():
    global budget
    try:
        budget = float(input("Enter your monthly budget: "))
        print(f"Monthly budget set to ₹{budget:.2f}\n")
    except ValueError:
        print("Invalid input. Please enter a number.\n")

def track_budget():
    if budget == 0:
        print("Please set a budget first.\n")
        return

    total_spent = sum(exp['amount'] for exp in expenses if isinstance(exp['amount'], (int, float)))

    print(f"Total expenses so far: ₹{total_spent:.2f}")
    if total_spent > budget:
        print("⚠️ You have exceeded your budget!\n")
    else:
        remaining = budget - total_spent
        print(f"You have ₹{remaining:.2f} left for the month.\n")

# Menu
def show_menu():
    print("====== Expense Tracker Menu ======")
    print("1. Add expense")
    print("2. View expenses")
    print("3. Set and track budget")
    print("4. Save expenses")
    print("5. Exit")

def main():
    load_expenses()

    while True:
        show_menu()
        try:
            choice = int(input("Enter your option (1-5): "))
            print()
            if choice == 1:
                add_expense()
            elif choice == 2:
                view_expenses()
            elif choice == 3:
                if budget == 0:
                    set_budget()
                track_budget()
            elif choice == 4:
                save_expenses()
            elif choice == 5:
                save_expenses()
                print("Exiting the program. Goodbye!")
                break
            else:
                print("Invalid option. Please choose 1–5.\n")
        except ValueError:
            print("Invalid input. Please enter a number.\n")

# Run the program
if __name__ == "__main__":
    main()
