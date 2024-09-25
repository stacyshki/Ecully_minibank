import csv
from os import remove


data = [
  ['Account number', 'Holder name', 'Balance', 'Card', 'Password'],
  ['000000001', 'admin', '0', '0', '(0_0)_SYSTEM_ADMINS$?>only_']
]

system_name = 'Ecully.csv'


def create_banking_system():
  with open(system_name, 'w') as file:
    writer = csv.writer(file)
    writer.writerows(data)


def delete_banking_system():
  remove(path=system_name)


def account_indexing(account_index):
  if type(account_index) != str:
    account_indexing = str(account_index)
  
  return account_indexing.zfill(9)


def card_number_creation(paying_system, account_number):
  bank = '20076'
  client_identification = account_number
  last_digit = luhn_algorithm(paying_system + bank + account_number + '0')
  card_number = paying_system + bank + client_identification + last_digit
  
  return card_number


def luhn_algorithm(card_number):
	digits_amount = len(card_number)
	numbers_sum = 0
	isSecond = False
	
	for i in range(digits_amount - 1, -1, -1):
		d = ord(card_number[i]) - ord('0')

		if isSecond:
			d *= 2
    
		numbers_sum += d // 10
		numbers_sum += d % 10
		isSecond = not isSecond
	
	return str(numbers_sum % 10)


def password_creation():
  password = input('\nEnter your password: ')
  
  while password.isalnum() or len(password) < 8:
    if password.isalnum():
      print('\nWeak password, please add symbols\n')
      password = input('Enter your password: ')
    else:
      print('\nWeak password, please make it longer\n')
      password = input('Enter your password: ')
  
  return password


def bank_asks_you():
  print('Enter the number if:\n\t1 - Create account\n\t2 - Delete account')
  print('\t3 - Check account info\n\t4 - Withdraw money\n\t5 - Deposit money')
  print('\t6 - Exit bank app\n')


def user_action_check(user_answer: str):
  if user_answer == '£ecully_administration_56833726$':
    return user_answer
  
  while not user_answer in ['1', '2', '3', '4', '5', '6']:
    print('\nThis number does not exist. Try one more time!\n')
    user_answer = input('\nEnter the number: ')
  return int(user_answer)
