#Kyle Frommelt 12-2-21 account_creator.py
import random
import os
import time
import csv
def create_new_account():
	account = ""

	while True:
		question = input('Would you like to create an account? Y/N: ').upper()
		if question == 'N':
			break
		else:
			pass
		first_name = input("Enter your first name: ")
		last_name = input('Enter your last name: ')
		gender = input('Enter your gender: ')
		age = input('Enter your age: ')
		ssn = input('Enter your social security number (ex: 111-11-1111): ')
		credit_score = input('Enter your credit score: ')
		salary = input('What is your estimated yearly salary: ')
		country = input('Enter your country: ')
		state = input('Enter your state: ')
		city = input('Enter your city: ')
		street = input('Enter your street and house number (ex: 123 Street): ')


		account_number = random.randint(1000000, 9999999)
		question2 = input('Will this be a joint account? Y/N: ').upper()
		if question2 == 'Y':
			account_number = str(account_number)+'1'
		else:
			pass
		exsisting_accounts = []
		file = open("exsisting_accounts.txt", "r")
		for i in file:
			if i == ",":
				exsisting_accounts.append(account)
				account = ""
			else:
				account = account + i
		file.close()
		if account_number in exsisting_accounts:
			pass
		else:
			exsisting_accounts.append(account_number)
			file = open("exsisting_accounts.txt", "a")
			file.write(str(account_number))
			file.write(",")
			file.close()
			break
	account_directory = str(account_number)
	os.mkdir(account_directory)
	file = open(str(account_directory) + "/balance.txt", "w")
	initial_deposit = input("What did the client deposit? : ")
	file.write(str(initial_deposit))
	file.close()

	file = open(str(account_directory) + "/history.txt", "w")
	file.write(str(time.asctime()))
	file.write(str("___$"))
	file.write(str(initial_deposit))
	file.close()
	return account_number

	file2 = open('proccessed_data.txt', 'w')
	file2.write('\n')
	file2.write(str(account_number)+','+(last_name)+','+(credit_score)+','+(country)+','+(gender)+','+(age)+','+(initial_deposit)+','+'1'+','+'0'+','+'1'+','+(salary)+','+'0'+',')
	file2.close()

	file3 = open('raw_bank_data.csv', 'a')
	file3.write('\n')
	file3.write(str(account_number)+','+(last_name)+','+(credit_score)+','+(country)+','+(gender)+','+(age)+','+(initial_deposit)+','+'1'+','+'0'+','+'1'+','+(salary)+','+'0'+',')
	file3.close()








