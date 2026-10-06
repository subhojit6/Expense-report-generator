print("=" * 25)
print("    FINANCE MANAGER    ")
print("=" * 25)

def show_menu():
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View transactions")
    print("4. Show balance")
    print("5. Exit")

transactions = []

while True:

    total_income = 0
    total_expenses = 0
    balance = 0

    show_menu()

    try:
        user_option = int(input("Chooose and option: "))
    except ValueError:
        print("=" * 25)
        print("Please enter a correct value")
        print("=" * 25)
        continue

    if user_option == 1:

        try:
            income = int(input("Enter amount: "))
        except ValueError:
            print("=" * 25)
            print("Please enter a correct income amount")
            print("=" * 25)
            continue
        source = input("Enter source: ")
        transactions.append({"amount": income, "source": source, "type": "income"})
        print("Income added successfully!")

    elif user_option == 2:
        try:
            amount = int(input("Enter amount: "))
        except ValueError:
            print("=" * 25)
            print("Please enter a correct expense amount")
            print("=" * 25)
            continue
        category = input("Enter category: ")
        transactions.append({"amount": amount, "category": category, "type": "expense"})
        print("Expense added successfully!")

    elif user_option == 3:
        for transaction in transactions:
            type = transaction["type"]
            if type == "income":
                print(f"Income: {transaction['amount']} | Source: {transaction['source']}")
            elif type == "expense":
                print(f"Expense: {transaction['amount']} | Category: {transaction['category']}")

    elif user_option == 4:
        for transaction in transactions:
            type = transaction["type"]

            if type == "income":
                total_income += transaction["amount"]
            elif type == "expense":
                total_expenses += transaction["amount"]
            balance = total_income - total_expenses

        print(f"Total Income: {total_income}")
        print(f"Total Expenses: {total_expenses}")
        print(f"Balance: {balance}")


    elif user_option == 5:
        print("Goodbye!")
        break
