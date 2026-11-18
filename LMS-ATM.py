import os
import pathlib
from datetime import datetime, date

class LoginSystem:
    def __init__(self):
        self.file = pathlib.Path("Admin_Credentials.csv")

        if not self.file.exists():
            with open(self.file, "w") as f:
                f.write("username,password\n")
                f.write("admin,Admin2026\n")

    def updateUsername(self, old_username, new_username):
        lines = []
        with open(self.file, "r") as f:
            for line in f:
                lines.append(line)

        header = lines[0]
        rows = lines[1:]
        updated_rows = []
        found = False

        for line in rows:
            info = line.strip().split(",")
            file_username, file_password = info[0], info[1]

            if file_username == old_username:
                file_username = new_username
                found = True

            updated_rows.append(f"{file_username},{file_password}\n")

        with open(self.file, "w") as f:
            f.write(header)
            for row in updated_rows:
                f.write(row)

        if found:
            print("Username updated successfully.")
        else:
            print("Username not found — no changes made.")

    def changePassword(self, username, new_password):
        lines = []
        with open(self.file, "r") as f:
            for line in f:
                lines.append(line)

        header = lines[0]
        rows = lines[1:]
        updated_rows = []
        found = False

        for line in rows:
            info = line.strip().split(",")
            file_username, file_password = info[0], info[1]

            if file_username == username:
                file_password = new_password
                found = True

            updated_rows.append(f"{file_username},{file_password}\n")

        with open(self.file, "w") as f:
            f.write(header)
            for row in updated_rows:
                f.write(row)

        if found:
            print("Password updated successfully.")
        else:
            print("Username not found — no changes made.")

    def checkLogin(self):
        print("Welcome to the administrator panel.")
        username = input("Please enter your username: ")
        password = input("Please enter your password: ")

        lines = []
        with open(self.file, "r") as f:
            for line in f:
                lines.append(line)

        rows = lines[1:]

        for line in rows:
            info = line.strip().split(",")
            file_username, file_password = info[0], info[1]

            if file_username == username and file_password == password:
                print(f"Login successful! Welcome, {file_username}.")
                return True

        print("Incorrect username or password, please try again.")
        return False


class AccountSystem:
    def __init__(self):
        self.file = pathlib.Path("Accounts.csv")

        if not self.file.exists():
            with open(self.file, "w") as f:
                f.write("accountnumber,pin,fullname,balance\n")
                f.write("1001,1234,Owen Ward,5000\n")
                f.write("1002,5678,Maria Santos,3000\n")

    def SearchAccount(self):
        accountnumber = input("Enter the account number to search: ")

        with open(self.file, "r") as f:
            for line in f.readlines()[1:]:
                if line.strip().split(",")[0] == accountnumber:
                    info = line.strip().split(",")
                    print(f"Account Number: {info[0]}")
                    print(f"Full Name: {info[2]}")
                    print(f"Balance: ₱{info[3]}")
                    return

        print(f"No account found with account number {accountnumber}.")

    def SearchByName(self):
        fullname = input("Enter the client's full name to search: ")

        with open(self.file, "r") as f:
            found = False
            for line in f.readlines()[1:]:
                info = line.strip().split(",")
                if info[2].lower() == fullname.lower():
                    found = True
                    print(f"Account Number: {info[0]}")
                    print(f"Full Name: {info[2]}")
                    print(f"Balance: ₱{info[3]}")

        if not found:
            print(f"No account found with name '{fullname}'.")

    def UpdateAccount(self):
        accountnumber = input("Enter the account number to update: ")

        with open(self.file, "r") as f:
            lines = f.readlines()

        updated_lines = []
        found = False

        for line in lines:
            if line.strip().split(",")[0] == accountnumber:
                found = True
                info = line.strip().split(",")

                print(f"Current PIN: {info[1]}")
                new_pin = input("Enter new PIN (leave blank to keep current): ")
                if new_pin:
                    info[1] = new_pin

                print(f"Current Full Name: {info[2]}")
                new_fullname = input("Enter new full name (leave blank to keep current): ")
                if new_fullname:
                    info[2] = new_fullname

                updated_lines.append(",".join(info) + "\n")
            else:
                updated_lines.append(line)

        if not found:
            print(f"No account found with account number {accountnumber}.")
            return

        with open(self.file, "w") as f:
            for line in updated_lines:
                f.write(line)

        print("Client record updated successfully.")

    def addAccount(self):
        accountnumber = input("Enter the new account number: ")

        with open(self.file, "r") as f:
            for line in f.readlines()[1:]:
                if line.strip().split(",")[0] == accountnumber:
                    print(f"Account number {accountnumber} already exists.")
                    return

        pin = input("Enter the new PIN: ")
        fullname = input("Enter the client's full name: ")
        try:
            balance = float(input("Enter the opening balance: "))
        except ValueError:
            print("Invalid amount entered. Account not registered.")
            return

        with open(self.file, "a") as f:
            f.write(f"{accountnumber},{pin},{fullname},{balance}\n")

        print("Client registered successfully.")

    def deleteAccount(self):
        accountnumber = input("Enter the account number to delete: ")

        with open(self.file, "r") as f:
            lines = f.readlines()

        header = lines[0]
        rows = lines[1:]
        updated_rows = []
        found = False

        for line in rows:
            info = line.strip().split(",")
            if info[0] == accountnumber:
                found = True
                continue
            updated_rows.append(line)

        if not found:
            print(f"No account found with account number {accountnumber}.")
            return

        with open(self.file, "w") as f:
            f.write(header)
            for row in updated_rows:
                f.write(row)

        print("Client record deleted successfully.")

    def getAccountRow(self, accountnumber):
        with open(self.file, "r") as f:
            for line in f.readlines()[1:]:
                info = line.strip().split(",")
                if info[0] == accountnumber:
                    return info
        return None

    def authenticate(self, accountnumber, pin):
        with open(self.file, "r") as f:
            for line in f.readlines()[1:]:
                info = line.strip().split(",")
                if info[0] == accountnumber and info[1] == pin:
                    return info
        return None

    def updateBalanceField(self, accountnumber, new_balance):
        with open(self.file, "r") as f:
            lines = f.readlines()

        header = lines[0]
        rows = lines[1:]
        updated_rows = []
        found = False

        for line in rows:
            info = line.strip().split(",")
            if info[0] == accountnumber:
                found = True
                info[3] = str(new_balance)
                updated_rows.append(",".join(info) + "\n")
            else:
                updated_rows.append(line)

        if found:
            with open(self.file, "w") as f:
                f.write(header)
                for row in updated_rows:
                    f.write(row)

        return found


class TransactionRecord:
    def __init__(self):
        self.file = pathlib.Path("Transactions.csv")

        if not self.file.exists():
            with open(self.file, "w") as f:
                f.write("accountnumber,type,amount,date,balanceafter\n")

    def addRecord(self, accountnumber, transaction_type, amount, balanceafter):
        with open(self.file, "a") as f:
            f.write(f"{accountnumber},{transaction_type},{amount},{date.today().isoformat()},{balanceafter}\n")

    def getRecordsForAccount(self, accountnumber):
        records = []

        with open(self.file, "r") as f:
            for line in f.readlines()[1:]:
                info = line.strip().split(",")
                if info[0] == accountnumber:
                    records.append(info)

        return records


def ClientLogin():
    print("Client Login selected.")
    accountnumber = input("Enter your account number: ")
    pin = input("Enter your PIN: ")

    account_system = AccountSystem()
    account_row = account_system.authenticate(accountnumber, pin)

    if account_row is None:
        print("Incorrect account number or PIN, please try again.")
        return None

    print(f"Login successful! Welcome, {account_row[2]}.")
    return account_row


def ViewAccountDetails(account_row):
    transaction_records = TransactionRecord()

    print(f"--- Account Details for {account_row[2]} (Account No: {account_row[0]}) ---")
    print(f"Current Balance: ₱{account_row[3]}")

    records = transaction_records.getRecordsForAccount(account_row[0])
    if records:
        print("Transaction History:")
        for record in records:
            print(f"  {record[3]} | {record[1]} | ₱{record[2]} | Balance After: ₱{record[4]}")
    else:
        print("Transaction History: none")


def WithdrawProcess(account_row):
    account_system = AccountSystem()
    transaction_records = TransactionRecord()

    try:
        amount = float(input("Enter the amount to withdraw: "))
    except ValueError:
        print("Invalid amount entered.")
        return account_row

    try:
        current_balance = float(account_row[3])
    except (ValueError, IndexError):
        print("Account data is corrupted for this entry.")
        return account_row

    if amount <= 0:
        print("Withdrawal amount must be greater than zero.")
        return account_row

    if amount > current_balance:
        print("Insufficient funds. Withdrawal cancelled.")
        return account_row

    new_balance = current_balance - amount
    account_system.updateBalanceField(account_row[0], new_balance)
    transaction_records.addRecord(account_row[0], "Withdrawal", amount, new_balance)

    account_row[3] = str(new_balance)
    print(f"You have successfully withdrawn ₱{amount}. New balance: ₱{new_balance}")
    return account_row


def DepositProcess(account_row):
    account_system = AccountSystem()
    transaction_records = TransactionRecord()

    try:
        amount = float(input("Enter the amount to deposit: "))
    except ValueError:
        print("Invalid amount entered.")
        return account_row

    try:
        current_balance = float(account_row[3])
    except (ValueError, IndexError):
        print("Account data is corrupted for this entry.")
        return account_row

    if amount <= 0:
        print("Deposit amount must be greater than zero.")
        return account_row

    new_balance = current_balance + amount
    account_system.updateBalanceField(account_row[0], new_balance)
    transaction_records.addRecord(account_row[0], "Deposit", amount, new_balance)

    account_row[3] = str(new_balance)
    print(f"You have successfully deposited ₱{amount}. New balance: ₱{new_balance}")
    return account_row


def TransferProcess(account_row):
    account_system = AccountSystem()
    transaction_records = TransactionRecord()

    destination_accountnumber = input("Enter the destination account number: ")

    if destination_accountnumber == account_row[0]:
        print("Cannot transfer to the same account.")
        return account_row

    destination_row = account_system.getAccountRow(destination_accountnumber)
    if destination_row is None:
        print(f"No account found with account number {destination_accountnumber}.")
        return account_row

    try:
        amount = float(input("Enter the amount to transfer: "))
    except ValueError:
        print("Invalid amount entered.")
        return account_row

    try:
        current_balance = float(account_row[3])
        destination_balance = float(destination_row[3])
    except (ValueError, IndexError):
        print("Account data is corrupted for this entry.")
        return account_row

    if amount <= 0:
        print("Transfer amount must be greater than zero.")
        return account_row

    if amount > current_balance:
        print("Insufficient funds. Transfer cancelled.")
        return account_row

    new_balance = current_balance - amount
    new_destination_balance = destination_balance + amount

    account_system.updateBalanceField(account_row[0], new_balance)
    account_system.updateBalanceField(destination_accountnumber, new_destination_balance)

    transaction_records.addRecord(account_row[0], f"Transfer to {destination_accountnumber}", amount, new_balance)
    transaction_records.addRecord(destination_accountnumber, f"Transfer from {account_row[0]}", amount, new_destination_balance)

    account_row[3] = str(new_balance)
    print(f"You have successfully transferred ₱{amount} to account {destination_accountnumber}. New balance: ₱{new_balance}")
    return account_row


def AdminPanel():
    print("Administrator Panel selected.")
    print("1. Search Client by Account Number")
    print("2. Search Client by Name")
    print("3. Update Client Record")
    print("4. Register New Client")
    print("5. Delete Client Record")
    print("6. Quit")

    choice = input("Please select an option: ")
    account_system = AccountSystem()

    if choice == "1":
        account_system.SearchAccount()

    if choice == "2":
        account_system.SearchByName()

    if choice == "3":
        account_system.UpdateAccount()

    if choice == "4":
        account_system.addAccount()

    if choice == "5":
        account_system.deleteAccount()

    if choice == "6":
        return


def UpdateAdminCredentials():
    print("Update Admin Credentials selected.")
    print("1. Update Username")
    print("2. Change Password")
    print("3. Quit")
    choice = input("Please select an option: ")

    admin_login = LoginSystem()

    if choice == "1":
        old_username = input("Enter your current username: ")
        new_username = input("Enter your new username: ")
        admin_login.updateUsername(old_username, new_username)
    elif choice == "2":
        username = input("Enter your username: ")
        new_password = input("Enter your new password: ")
        admin_login.changePassword(username, new_password)
    else:
        print("Invalid option, please try again.")

    if choice == "3":
        return


def ClientMenu(account_row):
    while True:
        print("Select the desired process:")
        print("1. View Account Details")
        print("2. Withdraw")
        print("3. Deposit")
        print("4. Transfer Funds")
        print("5. Logout")

        choice = input("Please select an option: ")

        if choice == "1":
            ViewAccountDetails(account_row)

        if choice == "2":
            account_row = WithdrawProcess(account_row)

        if choice == "3":
            account_row = DepositProcess(account_row)

        if choice == "4":
            account_row = TransferProcess(account_row)

        if choice == "5":
            print("Logging out...")
            return


def StartMenu():
    print("Welcome to the Command-Line ATM Simulation.")
    print("1. Client Login")
    print("2. Administrator Login")
    print("3. Quit")

    choice = input("Please select an option: ")

    if choice == "1":
        account_row = ClientLogin()
        if account_row is not None:
            ClientMenu(account_row)
        StartMenu()

    if choice == "2":
        admin_login = LoginSystem()
        if admin_login.checkLogin():
            while True:
                print("1. Admin Panel")
                print("2. Update Admin Credentials")
                print("3. Log Out")
                admin_choice = input("Please select an option: ")

                if admin_choice == "1":
                    AdminPanel()
                if admin_choice == "2":
                    UpdateAdminCredentials()
                if admin_choice == "3":
                    break
        StartMenu()

    if choice == "3":
        return


if __name__ == "__main__":
    StartMenu()