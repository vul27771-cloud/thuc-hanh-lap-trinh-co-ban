print("Sinh vien: LE TRONG TRUNG")
print("Ma so SV : 245751030110070")
print("############################")
###################################

class Bank:
    Account_type = "Savings"
    Location = "Guntur"

    def __init__(self, name, Account_Number, balance):
        self.name = name
        self.Account_Number = Account_Number
        self.balance = balance
        self.Account_type = Bank.Account_type
        self.Location = Bank.Location

    def __repr__(self):
        print("Welcome to the SBI ATM Machine")
        account_pin = int(input("Please enter your pin number: "))
        if account_pin == 123:
            self.Account()
        else:
            print("Pin Incorrect. Please try again")
            self.Error()
        return "{} {}".format(self.name, self.Account_Number)

    def Error(self):
        account_pin = int(input("Please enter your pin number: "))
        if account_pin == 123:
            self.Account()
        else:
            print("Pin Incorrect. Please try again")
            self.Error()

    def Account(self):
        print("Your Card Number is: XXXX XXXX XXXX 1337")
        print("Would you like to deposit/Withdraw/Check Balance?")
        print("""
        1) Balance
        2) Withdraw
        3) Deposit
        4) Quit
        """)
        option = int(input("Please enter your choice: "))
        if option == 1:
            self.Balance()
        elif option == 2:
            self.Withdraw()
        elif option == 3:
            self.Deposit()
        elif option == 4:
            self.Exit()

    def Balance(self):
        print("Balance:", self.balance)

    def Withdraw(self):
        withdraw = int(input("Please Enter Desired amount: "))
        if self.balance >= withdraw:
            self.balance -= withdraw
            print("Your transaction is successful")
            print("Your Balance:", self.balance)
        else:
            print("Your transaction is canceled due to insufficient balance")

    def Deposit(self):
        deposit = int(input("Please Enter Desired amount: "))
        self.balance += deposit
        print("Your transaction is successful")
        print("Balance:", self.balance)

    def Exit(self):
        print("Exit")

t1 = Bank("Nitesh", 1453210145, 5000)
print(t1)
