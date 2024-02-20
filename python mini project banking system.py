class Banking_system:
    def __init__(self, account_holder, pin, balance=0):
        self.account_holder = account_holder
        self.pin = pin
        self.balance = balance

    def login(self, entered_pin):
        return entered_pin == self.pin

    def deposit(self, amount):
        self.balance += amount
        return f"Deposited Rs{amount}. Current balance: Rs{self.balance}"

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return f"Withdraw Rs{amount}. Current balance: Rs{self.balance}"
        else:
            return "Insufficient fund."

def main():
    account_holder = "FATHIMA HIBA VP"
    pin = "9715"
    current_balance = 100000

    user_account = Banking_system(account_holder, pin, current_balance)

    # Login
    entered_pin = input("Enter your PIN: ")
    if user_account.login(entered_pin):
        print("successfully logged in,Welcome to federal Bank!")
    else:
        print("Incorrect PIN")
        return

    while True:
        print("\nselect your transaction:")
        print("1. Withdraw")
        print("2. Deposit")
        print("3. Exit")

        choice = input("Enter your transaction (1/2/3): ")

        if choice == "1":
            withdraw_amount = float(input("Enter the Withdrawal amount: "))
            print(user_account.withdraw(withdraw_amount))
        elif choice == "2":
            deposit_amount = float(input("Enter the Deposit amount: "))
            print(user_account.deposit(deposit_amount))
        elif choice == "3":
            print("Thank You for using our atm - federal bank")
            break
        else:
            print("Invalid option. Please enter 1, 2, or 3"
                  ".")

if __name__ == "__main__":
    main()