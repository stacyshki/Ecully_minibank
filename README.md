HOW TO WORK WITH A PROGRAM

1. Start main.py
2. Input what would you like to do
3. Provide information needed for the action
   (For example, provide your name and password
   to check account details)
4. Exit the app after the action or choose another
   action
5. Enjoy!

PROJECT FILES

1. The project has 4 files: banking_system.py,
   Ecully.csv, main.py, manage_accounts.py
2. Ecully.csv is the actual database, which keeps
   all information about bank users
3. File banking_system.py has 8 functions:
   3.1 The create_banking_system is a function
   that creates a CSV file named 'Ecully.csv'
   and writes the data stored in the data list
   into this file. The data includes information
   about account holders such as account number,
   holder name, balance, card number, and password.
   3.2 The delete_banking_system is a function
   that deletes the banking system file named
   'Ecully.csv' from the system. It uses the remove
   function from the os module to delete the file
   specified by the system_name variable.
   3.3 The account_indexing function is designed to
   take an account index as input and convert it into a
   9-digit string format by padding zeros to the left
   if necessary. If the input account index is not a
   string, it first converts it to a string and then
   pads zeros to make it a 9-digit string. This
   function ensures that account indexes are
   consistently formatted with leading zeros for proper
   indexing and identification within the banking
   system.
   3.4 The luhn_algorithm function is implementing the
   Luhn algorithm, also known as the Luhn formula or
   modulus 10 algorithm. This algorithm is used to
   validate identification numbers, such as credit card
   numbers, IMEI numbers, and more.
   3.5 The user_action_check function is designed to
   validate and check the user's input for bank
   actions. It takes a user's answer as a string
   parameter and ensures that the input is a valid
   option for bank actions. If the user's answer is
   not one of the predefined options ('1', '2', '3',
   '4', '5', '6'), it prompts the user to enter a
   valid number until a correct option is provided.
   Once a valid option is entered, the function
   returns the integer representation of the user's
   choice.
   3.6 The bank_asks_you function is displaying a set  
   of options for the user to choose from when
   interacting with the bank application. It prints
   out a menu with numbered options for various
   actions that the user can take within the banking
   system. The options include creating an account,
   deleting an account, checking account info,
   withdrawing money, depositing money, and exiting the
   bank app. This function serves as a user interface
   to guide the user on available actions and helps
   them navigate through the banking application by
   providing a clear list of choices.
   3.7 The password_creation function is responsible
   for generating a secure password for a user within
   the banking system.
   3.8 The card_number_creation function is
   responsible for generating a card number for a bank
   account holder based on the provided paying system
   and account number.

4. File manage_accounts has 10 functions:
   4.1 The load_accounts function is responsible
   for loading the existing accounts data from a
   CSV file into a dictionary. It reads the data
   from the file, processes it, and returns
   the accounts dictionary containing information
   such as account numbers, holder names, balances,
   card numbers, and passwords. If the file
   does not exist, it prints a message indicating
   that the banking system no longer exists and
   exits the program.
   4.2 The create_account function is responsible
   for creating a new account in the banking system.
   4.3 The delete_account function is responsible
   for deleting a user's account from the
   banking system.
   4.4 The deposit_money function is responsible
   for processing a deposit transaction for a
   user's account in the banking system.
   4.5 The withdraw_money function is responsible
   for processing a withdrawal transaction
   from a user's account in the banking system.
   4.6 The password_check function is responsible
   for verifying whether the password entered
   by the user matches the password associated
   with a specific account in the banking system.
   It takes two parameters: accounts, which
   is a dictionary containing account information,
   and index, which represents the index of
   the account for which the password needs
   to be checked.
   4.7 The admin_actions function is providing
   a set of options for the system owner to perform
   administrative tasks within the banking system.
   It displays a menu with the following options:
   create system, delete system, check users info
   4.8 The check_account_info function is
   responsible for retrieving and displaying
   the account information associated with a
   specific user in the banking system.
   4.9 The check_account_validity function
   is responsible for verifying the validity of
   a user's account within the banking system.
   It takes two parameters: accounts, which
   is a dictionary containing account information,
   and name, which represents the name of the
   account holder being checked.
   4.11 The write_accounts function is responsible
   for updating the accounts data stored in a
   CSV file. It takes a dictionary accounts as
   input, which contains the account information
   such as account numbers, holder names,
   balances, card numbers, and passwords

5. File main.py introduces a terminal interface
   with while user_answer != 6 statement is a
   while loop in Python. It will keep executing
   the codeblock inside the loop as long as the
   condition user_answer != 6 is true. In
   this specific context, the loop is controlling
   the flow of the banking system program based on
   the user's input
