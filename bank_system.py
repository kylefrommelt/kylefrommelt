import random
import account_creator
import os
import time
import schedule
import csv


class bank_account:
    def __init__(self):
        pass

    def look_up(self, account_number):
        account = ""
        exsisting_accounts = [] 
        file = open("exsisting_accounts.txt", "r")
        data = file.read()
        for i in data:
        	if i == ",":
        		exsisting_accounts.append(account)
        		account = ""
        	else:
        		account = account + i
        	file.close()
        if str(account_number) in exsisting_accounts:
        	print("It's there.")
        return exsisting_accounts

    def del_account(self, account_number, exsisting_accounts):
    	removing_balance = str(account_number)+"/balance.txt"
    	os.remove(removing_balance)
    	removing_history = str(account_number)+"/history.txt"
    	os.remove(removing_history)
    	os.removedirs(str(account_number))
    	exsisting_accounts.remove(str(account_number))
    	file = open("exsisting_accounts.txt", "w")
    	file.write(str(exsisting_accounts))
    	file.close()

    def interest(self, account_number):
        file = open(str(account_number)+"/balance.txt", 'r+')
        current_balance = file.read()
        float_balance = float(current_balance)
        balance_after_interest = float_balance * 1.7
        file.truncate(0)
        file.write(str(balance_after_interest))
        file.close()


    def account_creator(self):
        while True:
            account_number = random.randint(1000000, 9999999)
            if account_number in exsisting_accounts:
                pass
            else:
                exsisting_accounts.append(account_number)
                file = open("exsisting_accounts.txt", "a")
                file.write(str(account_number))
                file.write(",")
                file.close()
                break
        return account_number

    def deposit(self, account_number):
        file = open(str(account_number)+"/balance.txt", 'r+')
        balance = file.read()
        float_balance = float(balance)
        print('Your current balance is: '+balance)
        choice = float(input('Enter how much would you like to deposit: '))
        new_balance = float_balance + choice
        print('Your new current balance is: '+str(new_balance))
        file.truncate(0)
        file.write(str(new_balance))
        file.close()

        file2 = open(str(account_number)+'/history.txt', 'w')
        file2.write('\n')
        file2.write(str(current_time)+'  '+str(new_balance))
        file2.close()


    def withdraw(self, account_number):
        file = open(str(account_number)+"/balance.txt", 'r+')
        balance = file.read()
        float_balance = float(balance)
        print('Your current balance is: '+balance)
        choice = float(input('Enter how much would you like to withdraw: '))
        new_balance = float_balance - choice
        if choice <= float_balance:
            print('Your new current balance is: '+str(new_balance))
            file.truncate(0)
            file.write(str(new_balance))
        else:
            print('Error, you cannot overdraw your account')
        file.close()

        file2 = open(str(account_number)+'/history.txt', 'w')
        file2.write('\n')
        file2.write(str(current_time)+'  '+str(new_balance))
        file2.close()

a = bank_account()
current_time = time.ctime(time.time())
print(current_time)


choice = input("Do you have an existing account? Y/N >  ").upper()
if choice == "Y":
    account_number = int(input("Enter your account number:>  "))
    exsisting_accounts = a.look_up(account_number)
    choice2 = input("What do you want to do? 1 = Withdraw 2 = Deposit 3 = Close Account: ")
    if choice2 == "1":
    	a.withdraw(account_number)
    elif choice2 == "2":
    	a.deposit(account_number)
    elif choice2 == "3":
    	a.del_account(account_number, exsisting_accounts)
    a.update_csv(account_number)
elif choice == "N":
    a = bank_account()
    account_number = account_creator.create_new_account()
else:
    print("Error, please try again")

while True:
    schedule.every(30).days.do(a.interest(account_number))
else:
    pass
