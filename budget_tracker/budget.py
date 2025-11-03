from utils import input_float, input_nonempty

def add_expense(expenses):
    category = input_nonempty("Enter category (e.g., Food, Transport): ")
    amount = input_float("Enter amount: ")
    description = input("Enter description (optional): ")
    expense = {
        "category": category,
        "amount": amount,
        "description": description
    }
    expenses.append(expense)
    print("Expense added successfully!")

def remove_expense(expenses):
    list_expenses(expenses)
    try:
        index = int(input("Enter the number of the expense to remove: ")) - 1
        if 0 <= index < len(expenses):
            removed_expense = expenses.pop(index)
            print(f"Removed {removed_expense['category']} - ${removed_expense['amount']:.2f}")
        else:
            print("Invalid number!")
    except ValueError:
        print("Invalid input!")

def list_expenses(expenses):
    if not expenses:
        print("No expenses recorded")
        return
    print("\nYour expenses:")
    for i, exp in enumerate(expenses, 1):
        print(f"{i}. {exp['category']} - ${exp['amount']:.2f} ({exp['description']})")