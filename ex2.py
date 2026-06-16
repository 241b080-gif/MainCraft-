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

    category = input("Enter category (optional): ").strip()
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


def display_expenses():
    expenses = load_expenses()
    if not expenses:
        print("No expenses found. Add an expense first.\n")
        return

    print("\nSaved Expenses:")
    print("Date        | Description                 | Category      | Amount")
    print("------------+-----------------------------+---------------+---------")

    total = 0.0
    for expense in expenses:
        amount = float(expense["amount"])
        total += amount
        print(
            f"{expense['date']:<10} | {expense['description'][:25]:<25} | {expense['category'][:13]:<13} | ${amount:>7.2f}"
        )

    print("\nTotal amount spent: ${:.2f}\n".format(total))


def expense_summary():
    expenses = load_expenses()
    total = sum(float(expense["amount"]) for expense in expenses)
    count = len(expenses)

    print("\nExpense Summary:")
    print(f"Total entries: {count}")
    print(f"Total amount spent: ${total:.2f}")
    if count:
        print(f"Average expense: ${total / count:.2f}")
    print()


def show_menu():
    print("Expense Tracker")
    print("1. Add expense")
    print("2. View saved expenses")
    print("3. Show expense summary")
    print("4. Exit")


def main():
    while True:
        show_menu()
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            add_expense()
        elif choice == "2":
            display_expenses()
        elif choice == "3":
            expense_summary()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1, 2, 3, or 4.\n")


if __name__ == "__main__":
    main()
