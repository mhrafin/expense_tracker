
# Expense Tracker CLI

A simple, command-line-based application to help you track your expenses. Manage your spending by categorizing expenses, viewing summaries, and analyzing trends using visualizations. The program uses an Excel file to store and process your data, ensuring easy access and persistence.

## Features

- **Add an Expense:** Log your daily expenses with details like name, category, amount, and date.
- **View Expenses:** Display the last 7 entries or view all recorded expenses.
- **Analyze Spending:** See category-wise summaries of your total expenditures.
- **Visualize Data:** Generate bar charts to understand spending trends visually.
- **Categories:** Choose from predefined categories such as housing, food, transportation, entertainment, and more.

## Prerequisites

To run this program, you'll need:

- Python 3.x
- Required Python libraries: 
  - `pandas`
  - `openpyxl`
  - `matplotlib`

You can install the libraries using pip:
```bash
pip install pandas openpyxl matplotlib
```

## Usage

1. Clone this repository or download the source code.
2. Navigate to the project directory and run the main script:
   ```bash
   python main.py
   ```
3. Use the menu to interact with the program:
   - Add an expense.
   - View or analyze your expenses.
   - Visualize your spending trends.

## Expense Categories

The program includes the following predefined categories:
- Housing
- Utilities
- Transportation
- Food
- Healthcare
- Insurance
- Debt
- Savings
- Investment
- Personal Care
- Entertainment
- Leisure
- Education
- Childcare
- Gifts
- Donations
- Miscellaneous

## How It Works

1. **Data Storage:** Expenses are stored in an Excel file (`data/expense_tracker_dataset.xlsx`).
2. **Input Handling:** The user inputs expense details through prompts.
3. **Analysis:** The program calculates category-wise totals for insights.
4. **Visualization:** Spending trends are visualized using bar charts.

## Example

Here's a quick look at the program in action:

```plaintext
____________ Main Menu ____________

1. Add an Expense
2. Show Expense
3. Analysis
4. Visualize Analysis
5. Quit

Enter your choice: 1

____________ Add An Expense ____________

Enter the name of the expense: Groceries
Enter the amount: 150
Select an expense category: Food
Enter Date(YYYY-MM-DD): 2025-01-20
```
