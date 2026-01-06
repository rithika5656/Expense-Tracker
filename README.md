# 💰 Expense Tracker

A simple and elegant web-based expense tracker built with Python and Flask.

## Features

- ✅ Add income and expenses
- ✅ Categorize transactions (Salary, Food, Transport, etc.)
- ✅ View transaction history
- ✅ Monthly summary with income, expenses, and balance
- ✅ Delete transactions
- ✅ Beautiful, responsive UI
- ✅ Data persistence using JSON

## Screenshots

### Main Dashboard
- Summary cards showing total income, expenses, and balance
- Add transaction form
- Transaction history table

### Monthly Summary
- Month-wise breakdown of income and expenses
- Balance calculation for each month

## Tech Stack

- **Backend:** Python, Flask
- **Frontend:** HTML, CSS
- **Data Storage:** JSON file

## Installation

1. Clone the repository:
```bash
git clone https://github.com/rithika5656/Expense-Tracker.git
cd Expense-Tracker
```

2. Create a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
python app.py
```

5. Open your browser and navigate to:
```
http://localhost:5000
```

## Usage

1. **Add Transaction:** Fill in the date, type (income/expense), description, amount, and category, then click "Add Transaction"
2. **View Summary:** Click "View Monthly Summary" to see month-wise breakdown
3. **Delete Transaction:** Click the 🗑️ button next to any transaction to remove it

## Project Structure

```
Expense-Tracker/
├── app.py              # Main Flask application
├── data.json           # Data storage (auto-created)
├── requirements.txt    # Python dependencies
├── README.md          # Project documentation
├── templates/
│   ├── index.html     # Main page template
│   └── summary.html   # Monthly summary template
└── static/
    └── style.css      # Stylesheet
```

## License

This project is open source and available under the [MIT License](LICENSE).

## Author

Created with ❤️ by Rithika
