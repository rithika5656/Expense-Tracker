from flask import Flask, render_template, request, redirect, url_for, jsonify
import json
import os
from datetime import datetime

app = Flask(__name__)
DATA_FILE = 'data.json'

def load_data():
    """Load transactions from JSON file"""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return {'transactions': []}

def save_data(data):
    """Save transactions to JSON file"""
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=2)

@app.route('/')
def index():
    """Main page showing all transactions"""
    data = load_data()
    transactions = data['transactions']
    
    # Calculate totals
    total_income = sum(t['amount'] for t in transactions if t['type'] == 'income')
    total_expenses = sum(t['amount'] for t in transactions if t['type'] == 'expense')
    balance = total_income - total_expenses
    
    return render_template('index.html', 
                         transactions=transactions,
                         total_income=total_income,
                         total_expenses=total_expenses,
                         balance=balance)

@app.route('/add', methods=['POST'])
def add_transaction():
    """Add a new transaction"""
    data = load_data()
    
    transaction = {
        'id': len(data['transactions']) + 1,
        'date': request.form['date'],
        'description': request.form['description'],
        'amount': float(request.form['amount']),
        'type': request.form['type'],
        'category': request.form['category']
    }
    
    data['transactions'].append(transaction)
    save_data(data)
    
    return redirect(url_for('index'))

@app.route('/delete/<int:id>')
def delete_transaction(id):
    """Delete a transaction"""
    data = load_data()
    data['transactions'] = [t for t in data['transactions'] if t['id'] != id]
    save_data(data)
    return redirect(url_for('index'))

@app.route('/summary')
def monthly_summary():
    """Show monthly summary"""
    data = load_data()
    transactions = data['transactions']
    
    # Group by month
    monthly_data = {}
    for t in transactions:
        month_key = t['date'][:7]  # YYYY-MM format
        if month_key not in monthly_data:
            monthly_data[month_key] = {'income': 0, 'expenses': 0}
        
        if t['type'] == 'income':
            monthly_data[month_key]['income'] += t['amount']
        else:
            monthly_data[month_key]['expenses'] += t['amount']
    
    # Calculate balance for each month
    for month in monthly_data:
        monthly_data[month]['balance'] = monthly_data[month]['income'] - monthly_data[month]['expenses']
    
    # Sort by month
    sorted_months = sorted(monthly_data.items(), reverse=True)
    
    return render_template('summary.html', monthly_data=sorted_months)

if __name__ == '__main__':
    app.run(debug=True)
