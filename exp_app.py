from flask import Flask, request, jsonify
import json

app = Flask(__name__)
FILE_NAME = 'app_data.json'

# Load data from JSON file
def load_data():
    try:
        with open(FILE_NAME, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# Save data to JSON file
def save_data(data):
    with open(FILE_NAME, 'w') as file:
        json.dump(data, file, indent=4)

@app.route('/')
def home():
    return 'Expense Tracker API'

@app.route('/add', methods=['POST'])
def add_expense():
    data = request.get_json()
    expenses = load_data()
    expenses.append(data)
    save_data(expenses)
    return jsonify({'message': 'Record added successfully'})

@app.route('/view', methods=['GET'])
def view_expenses():
    return jsonify(load_data())

@app.route('/totals', methods=['GET'])
def view_totals():
    expenses = load_data()
    total_income = 0
    total_expenses = 0
    for exp in expenses:
        if exp['Type'] == "Income":
            total_income += exp['Amount']
        elif exp['Type'] == "Expense":
            total_expenses += exp['Amount']
    net_balance = total_income - total_expenses
    return jsonify({
        'Total Income': total_income,
        'Total Expenses': total_expenses,
        'Net Balance': net_balance
    })

if __name__ == '__main__':
    app.run(debug=True)