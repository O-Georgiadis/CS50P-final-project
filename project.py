import json
import sys

DATA_FILE = 'accounts.json'


def main():
    accounts_data = open_accounts()
    user_card = check_info(accounts_data)
    options(user_card, accounts_data)


def open_accounts():
    with open(DATA_FILE, 'r') as file:
        return json.load(file)


def save_accounts(accounts):
    with open(DATA_FILE, 'w') as file:
        json.dump(accounts, file, indent=4)


def check_info(accounts):
    while True:
        card_num = input('Please insert card number: ')
        card_pin = input('Please insert card pin: ')
        if len(card_num) != 16 or len(card_pin) != 3:
            print('Invalid card information')
            continue
        if card_num not in accounts:
            print('Card not registered, please contact the bank')
            sys.exit()
        if accounts[card_num]['pin'] != card_pin:
            print('Incorrect PIN, Try again.\n')
            continue
        print(f"Welcome, {card_num}!")
        return card_num


def options(card_num, accounts):
    while True:
        print('1 - Check Balance\n 2 - Deposit\n 3 - Withdraw\n 4 - View Transaction History\n 5 - Exit')
        try:
            choice = int(input('Enter choice from 1 to 5: '))
        except ValueError:
            print('Please enter a number')
            continue
        if choice == 1:
            check_balance(card_num, accounts)
        elif choice == 2:
            deposit(card_num, accounts)
        elif choice == 3:
            withdraw(card_num, accounts)
        elif choice == 4:
            transaction_history(card_num, accounts)
        else:
            exit()


def check_balance(card_num, accounts):
    balance = accounts[card_num]['balance']
    print(f"Your balance is {balance:.2f}€")
    return balance


def deposit(card_num, accounts, deposit_amount=None):
    if deposit_amount is None:
        try:
            deposit_amount = float(input('Enter amount to deposit: '))
        except ValueError:
            print('Invalid number')
            return
    if deposit_amount <= 0:
        print('Please enter a positive amount')
        return
    accounts[card_num]['balance'] += deposit_amount
    accounts[card_num]['transactions'].append(f"+{deposit_amount:.2f}€")
    save_accounts(accounts)
    print(f"Deposited amount {deposit_amount}€ Successfully!")


def withdraw(card_num, accounts, withdraw_amount=None):
    if withdraw_amount is None:
        try:
            withdraw_amount = float(input('Enter amount to withdraw: '))
        except ValueError:
            print('Invalid number')
            return
    if withdraw_amount <= 0:
        print('Please enter a positive amount')
        return
    if accounts[card_num]['balance'] < withdraw_amount:
        print('Not enough money')
        return

    accounts[card_num]['balance'] -= withdraw_amount
    accounts[card_num]['transactions'].append(f"-{withdraw_amount:.2f}€")
    save_accounts(accounts)
    print(f"Withdraw amount {withdraw_amount:.2f}€ Successfully")


def transaction_history(card_num, accounts):
    print('Transaction history: ')
    for i in accounts[card_num]['transactions']:
        print(i)


if __name__ == '__main__':
    main()

