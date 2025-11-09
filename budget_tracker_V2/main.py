import tkinter as tk
from tkinter import messagebox
from data import load_data, save_data


class BudgetApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Budget Tracker")
        self.root.geometry("500x500")

        self.expenses = load_data()

        tk.Label(root, text="Category:").pack()
        self.category_entry = tk.Entry(root)
        self.category_entry.pack()

        tk.Label(root, text="Amount:").pack()
        self.amount_entry = tk.Entry(root)
        self.amount_entry.pack()

        tk.Label(root, text="Description:").pack()
        self.description_entry = tk.Entry(root)
        self.description_entry.pack()

        tk.Button(root, text="Add Expense", command=self.add_expense).pack(pady=5)
        tk.Button(root, text="Remove Selected", command=self.remove_selected).pack(pady=5)
        tk.Button(root, text="Show Summary", command=self.show_summary).pack(pady=5)

        self.listbox = tk.Listbox(root, width=60, height=15)
        self.listbox.pack(pady=10)
        self.refresh_listbox()

        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

    def refresh_listbox(self):
        self.listbox.delete(0, tk.END)
        if not self.expenses:
            self.listbox.insert(tk.END, "No expenses yet.")
        else:
            for i, exp in enumerate(self.expenses, 1):
                line = f"{i}. {exp['category']} - ${exp['amount']:.2f} ({exp['description']})"
                self.listbox.insert(tk.END, line)

    def add_expense(self):
        category = self.category_entry.get().strip()
        amount_str = self.amount_entry.get().strip()
        desc = self.description_entry.get().strip()

        if not category or not amount_str:
            messagebox.showerror("Error", "Category and amount are required.")
            return

        try:
            amount = float(amount_str)
        except ValueError:
            messagebox.showerror("Error", "Amount must be a number.")
            return

        expense = {"category": category, "amount": amount, "description": desc}
        self.expenses.append(expense)
        self.refresh_listbox()
        self.category_entry.delete(0, tk.END)
        self.amount_entry.delete(0, tk.END)
        self.description_entry.delete(0, tk.END)

    def remove_selected(self):
        selection = self.listbox.curselection()
        if not selection:
            messagebox.showinfo("Info", "No expense selected.")
            return

        index = selection[0]
        if 0 <= index < len(self.expenses):
            removed = self.expenses.pop(index)
            messagebox.showinfo("Removed", f"Removed {removed['category']} - ${removed['amount']:.2f}")
            self.refresh_listbox()

    def show_summary(self):
        if not self.expenses:
            messagebox.showinfo("Summary", "No expenses yet.")
            return

        total = sum(e["amount"] for e in self.expenses)
        categories = {}
        for e in self.expenses:
            categories[e["category"]] = categories.get(e["category"], 0) + e["amount"]

        summary = f"Total spent: ${total:.2f}\n\nBy category:\n"
        for cat, amt in categories.items():
            summary += f"  {cat}: ${amt:.2f}\n"

        messagebox.showinfo("Summary Report", summary)

    def on_close(self):
        save_data(self.expenses)
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = BudgetApp(root)
    root.mainloop()