import csv
import os
import datetime

CSV_FILE = "expenses.csv"
FIELDNAMES = ["date", "description", "category", "amount"]

def ensure_csv_exists():
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, "w", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=FIELDNAMES)
            writer.writeheader()

def add_expense():
    ensure_csv_exists()
    description = input("Enter expense description: ").strip()
    if not description:
        description = "Unnamed expense"
        
    while True:
        amount_input = input("Enter amount spent: ").strip()
        try:
            amount = float(amount_input)
            break
        except ValueError:
            print("Invalid amount. Please enter a number like 12.50.")
            
    category = input("Enter category (e.g., Food, Travel, Shopping): ").strip()
    if not category:
        category = "General"
        
    date_input = input("Enter date (YYYY-MM-DD) or leave blank for today: ").strip()
    if date_input:
        try:
            expense_date = datetime.datetime.strptime(date_input, "%Y-%m-%d").date()
        except ValueError:
            print("Invalid date format. Using today instead.")
            expense_date = datetime.date.today()
    else:
        expense_date = datetime.date.today()
        
    with open(CSV_FILE, "a", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=FIELDNAMES)
        writer.writerow({
            "date": expense_date.isoformat(),
            "description": description,
            "category": category,
            "amount": f"{amount:.2f}",
        })
    print("Expense saved successfully.\n")

def load_expenses():
    ensure_csv_exists()
    with open(CSV_FILE, newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        return list(reader)

def print_expense_table(expenses):
    print("Date       | Description               | Category      | Amount")
    print("-----------+---------------------------+---------------+---------")
    for expense in expenses:
        amount = float(expense["amount"])
        print(
            f"{expense['date']:<10} | {expense['description'][:25]:<25} | {expense['category'][:13]:<13} | ${amount:>7.2f}"
        )

def display_expenses():
    expenses = load_expenses()
    if not expenses:
        print("No expenses found. Add an expense first.\n")
        return
    print("\nSaved Expenses:")
    print_expense_table(expenses)
    total = sum(float(expense["amount"]) for expense in expenses)
    print("\nTotal amount spent: ${:.2f}\n".format(total))

def search_by_category():
    expenses = load_expenses()
    if not expenses:
        print("No expenses found.\n")
        return
        
    search_term = input("Enter category to search for: ").strip().lower()
    matching_expenses = [e for e in expenses if e["category"].strip().lower() == search_term]
    
    if not matching_expenses:
        print(f"No expenses found matching category: '{search_term}'\n")
    else:
        print(f"\nExpenses in Category '{matching_expenses[0]['category']}':")
        print_expense_table(matching_expenses)
        total = sum(float(expense["amount"]) for expense in matching_expenses)
        print(f"Total spent in this category: ${total:.2f}\n")

def view_monthly_spending():
    expenses = load_expenses()
    if not expenses:
        print("No expenses found.\n")
        return
        
    monthly_totals = {}
    for expense in expenses:
        # Extract YYYY-MM from the date string
        month = expense["date"][:7] 
        amount = float(expense["amount"])
        monthly_totals[month] = monthly_totals.get(month, 0.0) + amount
        
    print("\nMonthly Spending Breakdown:")
    print("Month   | Total Spent")
    print("--------+------------")
    for month in sorted(monthly_totals.keys()):
        print(f"{month} | ${monthly_totals[month]:>9.2f}")
    print()

def expense_summary():
    expenses = load_expenses()
    total = sum(float(expense["amount"]) for expense in expenses)
    count = len(expenses)
    
    print("\nExpense Summary:")
    print(f"Total entries: {count}")
    print(f"Total amount spent: ${total:.2f}")
    if count:
        print(f"Average expense: ${total / count:.2f}")
        
        # Calculate breakdown per category
        category_totals = {}
        for expense in expenses:
            cat = expense["category"]
            amt = float(expense["amount"])
            category_totals[cat] = category_totals.get(cat, 0.0) + amt
            
        print("\nBreakdown by Category:")
        for cat, amt in category_totals.items():
            print(f" - {cat}: ${amt:.2f}")
    print()

def show_menu():
    print("Expense Tracker 2.0")
    print("1. Add expense")
    print("2. View all saved expenses")
    print("3. Search expenses by category")
    print("4. View monthly spending breakdown")
    print("5. Show full expense summary")
    print("6. Exit")

def main():
    while True:
        show_menu()
        choice = input("Choose an option (1-6): ").strip()
        if choice == "1":
            add_expense()
        elif choice == "2":
            display_expenses()
        elif choice == "3":
            search_by_category()
        elif choice == "4":
            view_monthly_spending()
        elif choice == "5":
            expense_summary()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1, 2, 3, 4, 5, or 6.\n")

if __name__ == "__main__":
    main()

```
