from datetime import datetime

# Step 1 & 2: Base and Derived Classes
class Transaction:
    def __init__(self, amount, category):
        if amount <= 0:
            raise ValueError("Amount must be positive!")
        self.amount = amount
        self.category = category
        self.date = datetime.now()

    def apply(self, account):
        raise NotImplementedError("Subclasses must implement apply()")


class Income(Transaction):
    def apply(self, account):
        account._balance += self.amount


class Expense(Transaction):
    def apply(self, account):
        account._balance -= self.amount


# Step 3: Encapsulation
class Account:
    def __init__(self):
        self._balance = 0.0
        self._transactions = []

    def add_transaction(self, transaction):
        transaction.apply(self)
        self._transactions.append(transaction)

    def get_balance(self):
        return self._balance

    def get_transactions(self):
        return self._transactions


# Step 4: Report Generation
class ReportGenerator:
    def generate_report(self, account):
        transactions = account.get_transactions()
        total_income = sum(t.amount for t in transactions if isinstance(t, Income))
        total_expense = sum(t.amount for t in transactions if isinstance(t, Expense))

        print("\n--- Financial Report ---")
        print(f"Total Income  : Rs. {total_income:.2f}")
        print(f"Total Expenses: Rs. {total_expense:.2f}")
        print(f"Net Savings   : Rs. {total_income - total_expense:.2f}")
        print("\nDetailed Transactions:")
        print(f"{'Type':<10}{'Category':<15}{'Amount':<10}{'Date'}")
        print("-" * 50)

        for t in transactions:
            type_name = "Income" if isinstance(t, Income) else "Expense"
            print(f"{type_name:<10}{t.category:<15}Rs. {t.amount:<10.2f}{t.date.strftime('%Y-%m-%d %H:%M:%S')}")

        print("-" * 50)
        print()



# Step 5: User Interface
def main():
    account = Account()
    report = ReportGenerator()

    while True:
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Report")
        print("4. Exit")
        choice = input("Choose option: ")

        if choice == '1':
            amount = float(input("Enter income amount: "))
            category = input("Enter category: ")
            account.add_transaction(Income(amount, category))

        elif choice == '2':
            amount = float(input("Enter expense amount: "))
            category = input("Enter category: ")
            account.add_transaction(Expense(amount, category))

        elif choice == '3':
            report.generate_report(account)

        elif choice == '4':
            print("Goodbye!")
            break

        else:
            print("Invalid option!\n")


if __name__ == "__main__":
    main()
