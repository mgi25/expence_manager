# Simple Expense Manager

expenses = []

while True:
    print("\n--- Expense Manager ---")
    print("1. Add Expense/Income")
    print("2. View All Records")
    print("3. View Totals")
    print("4. Exit")
    
    choice = input("Choose an option: ")
    
    if choice == "1":
        record_type = input("Enter type (Expense/Income): ").capitalize()
        date = input("Enter date (YYYY-MM-DD): ")
        category = input("Enter category (e.g., Food, Salary, etc.): ")
        amount = float(input("Enter amount: "))
        description = input("Enter description: ")
        
        record = {
            "Type": record_type,
            "Date": date,
            "Category": category,
            "Amount": amount,
            "Description": description
        }
        expenses.append(record)
        print("Record added successfully!")
    
    elif choice == "2":
        print("\n--- All Records ---")
        for i, expense in enumerate(expenses, start=1):
            print(f"{i}. {expense['Type']} | {expense['Date']} | {expense['Category']} | {expense['Amount']} | {expense['Description']}")
    
    elif choice == "3":
        total_income = sum(expense['Amount'] for expense in expenses if expense['Type'] == "Income")
        total_expenses = sum(expense['Amount'] for expense in expenses if expense['Type'] == "Expense")
        net_balance = total_income - total_expenses

        print("\n--- Totals ---")
        print(f"Total Income: {total_income}")
        print(f"Total Expenses: {total_expenses}")
        print(f"Net Balance: {net_balance}")
    
    elif choice == "4":
        print("Exiting the program. Goodbye!")
        break
    
    else:
        print("Invalid option. Please try again.")
