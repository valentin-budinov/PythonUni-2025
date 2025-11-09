from collections import defaultdict

def show_summary(expenses):
    if not expenses:
        print("No data to summarize.")
        return

    total = sum(e["amount"] for e in expenses)
    print(f"\nTotal spent: ${total:.2f}")

    by_category = defaultdict(float)
    for e in expenses:
        by_category[e["category"]] += e["amount"]

    print("\nSpending by category:")
    for category, amount in by_category.items():
        print(f"{category}: ${amount:.2f} ({amount/total*100:.1f}%)")