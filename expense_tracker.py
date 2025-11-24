import matplotlib.pyplot as plt

expenses = []

def add_expense():
    amount = float(input("Enter amount spent: "))
    description = input("Enter description: ")
    expenses.append({'amount': amount, 'description': description})
    print("Expense added!\n")

def view_expenses():
    if not expenses:
        print("No expenses recorded.\n")
        return
    print("\nList of expenses:")
    for idx, exp in enumerate(expenses, 1):
        print(f"{idx}. ₹{exp['amount']}  -- {exp['description']}")
    print()

def show_total():
    total = sum(exp['amount'] for exp in expenses)
    print(f"\nTotal spent: ₹{total}\n")

def plot_graph():
    if not expenses:
        print("No expenses to plot!\n")
        return
    amounts = [exp['amount'] for exp in expenses]
    plt.plot(range(1, len(amounts)+1), amounts, marker='o')
    plt.title("Expense Variation")
    plt.xlabel("Expense Number")
    plt.ylabel("Amount (₹)")
    plt.grid(True)
    plt.show()

def main():
    while True:
        print("Expense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Show Total Spent")
        print("4. Plot Expenses Graph")
        print("5. Exit")
        choice = input("Choose an option (1-5): ")
        
        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            show_total()
        elif choice == '4':
            plot_graph()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
