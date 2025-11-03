from budget import add_expense, remove_expense, list_expenses
from data import load_data, save_data
from report import show_summary

def main():
    expenses = load_data()
    while True:
        print("\n=== Budget Tracker ===")
        print("1. Add expense")
        print("2. View expenses")
        print("3. Remove expense")
        print("4. Summary report")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            list_expenses(expenses)
        elif choice == "3":
            remove_expense(expenses)
        elif choice == "4":
            show_summary(expenses)
        elif choice == "5":
            save_data(expenses)
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()