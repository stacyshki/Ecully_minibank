import banking_system as bank
import manage_accounts as acc
from time import sleep

print('Hello!\nThis is bank ECULLY!\nWhat would you like to do?')
bank.bank_asks_you()
user_answer = input('\nEnter the number: ')
user_answer = bank.user_action_check(user_answer)

while user_answer != 6:
  
  if user_answer == 1:
    print(acc.create_acount())
  elif user_answer == 2:
    print(acc.delete_account())
  elif user_answer == 3:
    print(acc.check_account_info())
  elif user_answer == 4:
    withdrawal = input('\nEnter how much money would you like to withdraw: ')
    
    if withdrawal.isdigit():
      print(acc.withdraw_money(int(withdrawal)))
    else:
      print('\nSorry, invalid withdrawal amount\n')
  elif type(user_answer) == str:
    print(acc.admin_actions())
  else:
    deposit = input('\nEnter how much money would you like to deposit: ')
    
    if deposit.isdigit():
      print(acc.deposit_money(int(deposit)))
    else:
      print('\nSorry, invalid deposit amount\n')
  
  sleep(3)
  bank.bank_asks_you()
  user_answer = input('Enter the number: ')
  user_answer = bank.user_action_check(user_answer)

print('\nThanks for using our app! Have a good day!')
