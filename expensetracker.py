from flask import Flask, jsonify
from flask_cors import CORS
import pandas as pd

app = Flask(__name__)
CORS(app, origins=["http://localhost:5173"])  

@app.route('/summary', methods=['GET'])
def summary():   
    filename = "first.csv"  

    try:
        df = pd.read_csv(filename)
    except FileNotFoundError:
        return jsonify(["CSV file not found."])

#removing all of the commas
    df['Deposits'] = df["Deposits"].replace(',', '', regex=True)
    df['Deposits'] = pd.to_numeric(df['Deposits'], errors='coerce')
    df['Withdrawls'] = df["Withdrawls"].replace(',', '', regex=True)
    df['Withdrawls'] = pd.to_numeric(df['Withdrawls'], errors='coerce')

    output = []


#grouping da deposits with da descriptions
    output.append("Total deposits per description:")
    deposits = df.groupby('Description')['Deposits'].sum()
    for desc, amount in deposits.items():
        output.append(f"{desc}: ${float(amount):.2f}")

    output.append("Total withdrawals per description:")
    withdrawals = df.groupby('Description')['Withdrawls'].sum()
    for desc, amount in withdrawals.items():
        output.append(f"{desc}: ${float(amount):.2f}")

    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True, port=5050)














# def get_expense_summary(transactions):
#     deposit_count = 0
#     withdrawal_count = 0

#     for t in transactions:
#         description = t['description'].lower()
#         amount = t['amount']
#         if "deposit" in description:
#             deposit_count += amount
#         elif "withdrawal" in description:
#             withdrawal_count += amount

#     summary = f"Total Deposits: ${deposit_count:.2f}\nTotal Withdrawals: ${withdrawal_count:.2f}"
#     return summary




##def main():
#        tracker= ExpenseTracker()
#
#        while True:
 #           print("\nExpense Tracker Menu")
 #           print("1. add expense")
  #          print("2. remove expense")
   #         print("3. view expenses")
 #           print("4. total expenses ")
#            print("leave")

 #           choice = input("Enter your choice (1-5):")
 #           if choice == "1":
 #               date = input("Enter the date (YYYY-MM-DD)")
 #               description = input("Enter the description: ")
 #               amount = float(input("Enter the amount: "))
 #               expense = Expense(date, description, amount)
 #               tracker.add_expense(expense)
 #               print("expense added successfully")
 #           elif choice == "2":
 #               index = int(input(" enter the index number to remove: ")) -1 
 #               tracker.remove_expense(index)
 #           elif choice == "3":
 #               tracker.view_expenses()
  #          elif choice == "4":
 #               tracker.total_expenses()
 #           elif choice == "5":
 #               print( "ok lit")
 #               break 
 #           else:
 #               print ("idk what u are trying to say")

