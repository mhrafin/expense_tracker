import sys
import os.path
import pandas as pd
import time
import matplotlib.pyplot as plt


from datetime import datetime
from expense import expense


# path = "expense_tracker_dataset.xlsx"
def main():
    os.system("clear")

    path = "data/expense_tracker_dataset.xlsx"

    print(f"\n____________ Main Menu ____________\n")
    # check if the file exist, else create it
    check_file(path)

    print("""
1. Add an Expense
2. Show Expense
3. Analysis
4. Visualize Analysis
5. Quit
""")
    choice = int(input(f"Enter your Choice: "))
    if choice not in [1, 2, 3, 4, 5]:
        print(f"Invalid Input. Try Again")
        main()

    if choice == 1:
        # Take user input including choosing category
        new_expense = take_input()

        # Store/Append it into a file
        add_to_file(new_expense, path)
    elif choice == 2:
        # Show the data
        show_expenses(path)
    elif choice == 3:
        # Show analysis of the data
        analyze_data(path)
    elif choice == 4:
        visualize_data(path)
    elif choice == 5:
        quit()

    # Show reports
    # visualize_data()

    ## Income Management

    # Quit


def check_file(file_path):
    if os.path.isfile(file_path):
        pass
    else:
        titles = ["Name", "Category", "Amount", "Date"]
        titles_df = pd.DataFrame(columns=titles)
        titles_df.to_excel(file_path, index=False)


def select_category(return_cat_list: bool = False):
    category_list = [
        "Housing",
        "Utilities",
        "Transportation",
        "Food",
        "Healthcare",
        "Insurance",
        "Debt",
        "Savings",
        "Investment",
        "Personal Care",
        "Entertainment",
        "Leisure",
        "Education",
        "Childcare",
        "Gifts",
        "Donations",
        "Misc",
    ]
    category_list.sort()
    if return_cat_list:
        return category_list

    # Displaying the list
    for i, item in enumerate(category_list, start=1):
        print(f"{i}. {item}")

    try:
        choice = int(input("\nYour Choice: "))
    except ValueError:
        print("InValid Input. Enter a valid Choice.")
        return select_category()

    if choice < 1 or choice > len(category_list):
        print("Your choice is out of range. Enter a valid choice.")
        return select_category()
    else:
        return category_list[choice - 1]


def take_input():
    os.system("clear")
    print("\n____________ Add An Expense ____________\n")

    expense_name = input("Enter the name of the expense: ")
    expense_amount = float(input(f"Enter the amount: "))
    print("\nSelect an expense category: ")
    expense_category = select_category()
    try:
        expense_date = datetime.strptime(
            input("\nEnter Date(YYYY-MM-DD): "), "%Y-%m-%d"
        ).date()
        # print(expense_date)
    except ValueError:
        print("\nWrong Format or Invalid Input\n")
        main()

    # Debugging
    # print(f"\nYou have entered:\nName: {expense_name}\nAmount: {expense_amount}\nCategory: {expense_category}\nDate: {expense_date}\n")

    new_expense = expense(expense_date, expense_category, expense_name, expense_amount)

    return new_expense


def add_to_file(new_expense: expense, file_path):
    # os.system("clear")
    # print(f"Add to file Function")
    name = new_expense.name
    category = new_expense.category
    amount = new_expense.amount
    date = new_expense.date

    new_entry = {
        "Name": [name],
        "Category": [category],
        "Amount": [amount],
        "Date": [date],
    }
    # print(new_entry)
    new_df = pd.DataFrame(new_entry)

    with pd.ExcelWriter(
        file_path, engine="openpyxl", mode="a", if_sheet_exists="overlay"
    ) as writer:
        new_df.to_excel(
            writer,
            sheet_name="Sheet1",
            startrow=writer.sheets["Sheet1"].max_row,
            index=False,
            header=False,
        )

    main()


def show_expenses(file_path):
    os.system("clear")
    print(f"\n____________ Expenses ____________\n")

    print(f"1. Last 7 Entry\n2. All Entries\n3. Main Menu")

    choice = input(f"Enter Your Choice: ")

    df = pd.read_excel(
        file_path,
        dtype={"Name": str, "Category": str, "Amount": float},
        parse_dates=["Date"],
    )

    if choice == "1":
        print(df.tail(7))
    elif choice == "2":
        print(df)
    elif choice == "3":
        main()
    else:
        print(f"Invalid Choice. Try Again.")
        time.sleep(1)
        show_expenses(file_path)

    try:
        back = int(input(f"\nEnter 1 to go Back: "))
    except ValueError:
        print("ValueError: Returning to Main Menu")
        time.sleep(1)
        main()

    if back == 1:
        show_expenses(file_path)


def analyze_data(file_path):
    os.system("clear")
    print(f"\n____________ Analysis ____________\n")

    df = pd.read_excel(
        file_path,
        dtype={"Name": str, "Category": str, "Amount": float},
        parse_dates=["Date"],
    )

    # print(df)
    category_list = select_category(True)
    # print(category_list)
    # print(df["Category"])

    print(f"Total Spent on Each Category")
    for item in category_list:
        item_rows = df[df["Category"] == item]
        # print(f"\n{x}\n")
        if item_rows["Amount"].sum() > 0.0:
            print(f"{item}: {item_rows['Amount'].sum()}")

    input("\nPress Any Key to go to Main Menu\n")
    main()


def visualize_data(file_path):
    os.system("clear")
    print(f"\n____________ Visualization ____________\n")

    df = pd.read_excel(
        file_path,
        dtype={"Name": str, "Category": str, "Amount": float},
        parse_dates=["Date"],
    )

    category_list = select_category(True)

    dict_for_plot: dict = {}

    # print(f"Total Spent on Each Category")
    for item in category_list:
        item_rows = df[df["Category"] == item]
        # print(f"\n{x}\n")
        if item_rows["Amount"].sum() > 0.0:
            dict_for_plot[item] = item_rows["Amount"].sum()
            # print(f"{item}: {item_rows["Amount"].sum()}")
    # print(dict_for_plot)
    viz_df = pd.DataFrame.from_dict(dict_for_plot, orient="index", columns=["Total"])

    # print(viz_df)

    viz_df.plot.bar()

    plt.show(block=False)
    os.system("clear")
    input("\nPress Any Key to go to Main Menu\n")
    main()


def quit():
    os.system("clear")
    print(f"Quiting")

    print(".")
    time.sleep(0.15)
    print(".")
    time.sleep(0.29)
    print(".")
    time.sleep(0.57)
    sys.exit()


if __name__ == "__main__":
    main()
