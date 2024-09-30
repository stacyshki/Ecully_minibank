import csv
import banking_system as bank
from sys import exit

accounts_amount = 0


def load_accounts():
  global accounts_amount
  
  try:
    with open(bank.system_name, 'r') as file:
      account_reader = csv.DictReader(file)
      accounts = dict()
      
      for account in account_reader:
        for key, value in account.items():
          if key in accounts.keys():
            accounts[key].append(value)
          else:
            accounts[key] = [value]
      
      accounts_amount = int(accounts['Account number'][-1].lstrip('0'))
      return accounts
  except FileNotFoundError:
    print('\nSorry, our banking system no more exists\n')
    exit()


def create_acount():
  global accounts_amount
  accounts = load_accounts()
  name = input('\nPlease, enter your name and surname: ')
  
  if check_account_validity(accounts, name):
    return '\nAccount already exists\n'
  else:
    accounts_amount += 1
    index = bank.account_indexing(accounts_amount)
    paying_system = input('\nWhat paying system would you like to choose:'
                          'Visa or Mastercard? (type 5 or 2 respectively): ')
    
    if paying_system not in ['5', '2']:
      return '\nThis payment system does not exist\n'
    
    accounts['Balance'].append(0)
    accounts['Holder name'].append(name)
    accounts['Account number'].append(index)
    accounts['Card'].append(bank.card_number_creation(paying_system, index))
    accounts['Password'].append(bank.password_creation())
    write_accounts(accounts)
    return '\nAccount successfully created\n'


def delete_account():
  accounts = load_accounts()
  name = input('\nPlease, enter your name and surname: ')
  
  if check_account_validity(accounts, name):
    index = accounts['Holder name'].index(name)
    
    if password_check(accounts, index):
      for key in accounts.keys():
        del accounts[key][index]
      
      write_accounts(accounts)
      return '\nAccount successfully deleted\n'
    return '\nInvalid password\n'
  
  return '\nAccount does not exist\n'


def check_account_info():
  accounts = load_accounts()
  name = input('\nEnter your name and surname: ')
  
  if check_account_validity(accounts, name):
    index = accounts['Holder name'].index(name)
    
    if password_check(accounts, index):
      data_string = '\n'
      
      for i in accounts.keys():
        data_string += f'\t{i}: {accounts[i][index]}\n'
      
      return data_string
    else:
      return '\nInvalid password\n'
  
  return '\nAccount does not exist\n'


def withdraw_money(withdrawal: int):
  accounts = load_accounts()
  name = input('\nEnter your name and surname: ')
  if check_account_validity(accounts, name):
    index = accounts['Holder name'].index(name)
    
    if int(accounts['Balance'][index]) >= withdrawal:
      if password_check(accounts, index):
        accounts['Balance'][index] = int(accounts['Balance'][index])-withdrawal
        write_accounts(accounts)
        return '\nMoney withdraw done successfully\n'
      else:
        return '\nInvalid password\n'
    else:
      return '\nNot enough money\n'
  return '\nAccount does not exist\n'


def deposit_money(deposit: int):
  accounts = load_accounts()
  name = input('\nEnter your name and surname: ')
  
  if check_account_validity(accounts, name):
    index = accounts['Holder name'].index(name)
    
    if password_check(accounts, index):
      accounts['Balance'][index] = int(accounts['Balance'][index]) + deposit
      write_accounts(accounts)
      return '\nMoney were deposited successfully\n'
    else:
      return '\nInvalid password\n'
  
  return '\nAccount does not exist\n'


def write_accounts(accounts):
  with open(bank.system_name, 'w', newline='') as file:
    writer = csv.DictWriter(file, accounts.keys())
    writer.writeheader()
    
    for index in range(len(accounts['Account number'])):
      new_row = {}
      
      for key in accounts.keys():
        new_row[key] = accounts[key][index]
      
      writer.writerow(new_row)


def check_account_validity(accounts, name):
  if type(accounts) == str:
    return False
  
  if name in accounts['Holder name']:
    return True
  
  return False


def admin_actions():
    print('Hello, owner! What would u like to do?: ')
    print('\t1 - Create system\n\t2 - Delete system\n\t3 - Check users info\n')
    admin_request = input('Enter the number: ')
    if admin_request in ['1', '2', '3']:
      match admin_request:
        case '1' : bank.create_banking_system()
        case '2' : bank.delete_banking_system()
        case '3' : print(load_accounts(), end='\n\n')
      return 'Success!\n'
    else:
      return 'Something went wrong...\n'


def password_check(accounts, index):
  password = input('\nEnter your password: ')
  return accounts['Password'][index] == password
