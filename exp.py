import json
import os

def show_menu():
    print("1. List of transactions")
    print("2. New Transactions")
    print("3. Total summary")
    print("4. Analysis")
    print("5. Exit")
    choice = int(input("Enter choice: "))
    return choice

def new_transaction():
    type = int(input('Enter 1 for Income and 2 for Expense: '))
    category = input("Enter Category: ")
    amount = float(input("Enter amount: "))
    description = input("Enter description: ")
    return type, category, amount, description

# Load the data from a file
if os.path.exists("data.json"):
    print("Data exists... loading")
    with open('data.json', 'r') as file:
        expense_data = {'income': [], 'expenses': []}
else:
    print("New program... initializing")
    expense_data = {'income': [], 'expenses': []}

# Main program
while True:
    choice = show_menu()
    
    if choice == 1:
        print("List")
    elif choice == 2:
        type, category, amount, description = new_transaction()
        transaction_details = {
            'category': category,
            'amount': amount,
            'description': description
        }
        if type == 1:
            expense_data['income'].append(transaction_details)
        elif type == 2:
            expense_data['expenses'].append(transaction_details)
        else:
            print("Invalid type! Could not add the last transaction: ", transaction_details.__str__())
    elif choice == 3:
        print("Summary")
    elif choice == 4:
        print("Analytics")
    elif choice == 5:
        with open('data.json', 'w') as file:
            json.dump(expense_data, file)
        print("Exiting....")
        break
