# importing modules

import datetime

import os


# create a welcome function which presents the admin with a navigation menu
#def admin_menu()


def admin():
# File paths
super_admin_file_path = "super_admin_data.txt"
admin_file_path = "admin_data.txt"
staff_file_path = "staff_data.txt"

# Function to read credentials from a file
def read_credentials(file_path):
    credentials = {}
    try:
        with open(file_path, "r") as file:
            for line in file:
                username, password = line.strip().split(',')
                credentials[username] = password
    except FileNotFoundError:
        # Create the file if it doesn't exist
        open(file_path, "w").close()
    return credentials

# Function to validate login
def login(role, username, password):
    credentials = read_credentials(role)
    if username in credentials and credentials[username] == password:
        return True
    else:
        return False

# Function to register a new user
def register(role, username, password):
    credentials = read_credentials(role)
    if username not in credentials:
        with open(role, "a") as file:
            file.write(f"{username},{password}\n")
        print(f"Registration successful for {role} {username}.")
    else:
        print(f"Error: {role} {username} already exists.")

# Ask the user for their role
user_role = input("Enter your role (admin/super_admin/staff): ").lower()

# Handle registration or login based on the user's role
if user_role == "admin":
    print("Admin Login or Register")
    action = input("Do you want to login or register? ").lower()
    if action == "login":
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        if login(admin_file_path, username, password):
            print("Login successful! Welcome Admin.")
            # Add your admin functionality here
        else:
            print("Login failed. Invalid username or password.")
    elif action == "register":
        username = input("Enter a new username: ")
        password = input("Enter a new password: ")
        register(admin_file_path, username, password)
    else:
        print("Invalid action. Please enter 'login' or 'register'.")
elif user_role == "super_admin":
    print("Super Admin Login or Register")
    action = input("Do you want to login or register? ").lower()
    if action == "login":
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        if login(super_admin_file_path, username, password):
            print("Login successful! Welcome Super Admin.")
            # Add your super admin functionality here
        else:
            print("Login failed. Invalid username or password.")
    elif action == "register":
        username = input("Enter a new username: ")
        password = input("Enter a new password: ")
        register(super_admin_file_path, username, password)
    else:
        print("Invalid action. Please enter 'login' or 'register'.")
elif user_role == "staff":
    print("Staff Login or Register")
    action = input("Do you want to login or register? ").lower()
    if action == "login":
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        if login(staff_file_path, username, password):
            print("Login successful! Welcome Staff.")
            # Add your staff functionality here
        else:
            print("Login failed. Invalid username or password.")
    elif action == "register":
        username = input("Enter a new username: ")
        password = input("Enter a new password: ")
        register(staff_file_path, username, password)
    else:
        print("Invalid action. Please enter 'login' or 'register'.")
else:
    print("Invalid role. Please enter 'admin', 'super_admin', or 'staff'.")


# create a welcome function which presents the customer with a navigation menu
def customer_menu():
    print('-------------------------------')
    print('Welcome To OTAN Bank!')
    print('How may we help you today? Please choose from the following:')
    print('1 - Sign Up for an account')
    print('2 - Login to your account')
    print('3 - Exit')


def welcome():
    print("Welcome to OTAN Bank. Please select an option:")
    print('1 - Super Admin Menu')
    print('2 - Admin Staff Menu')
    print('3 - Staff Menu')
    print('4 - Customer Menu')
    option = int(input('Please choose an option from the menu: '))

    if option == 1:
        pin = input("Please enter the Admin's password: ")

        if pin == str("0000"):
            admin()
        else:
            print("Invalid password; please try again!")
            welcome()
    elif option == 4:
        customer_menu()
    else:
        print("Please enter a valid choice!")
        welcome()
welcome()


accnum = 0



#def get_accnum():
 #   try:
  #      with open('accnum.txt', 'r') as file:
   #         return int(file.read())
    #except FileNotFoundError:
     #   return 0
def get_accnum():
    try:
        with open('accnum.txt', 'r') as file:
            content = file.read().strip()
            return int(content) if content else 0
    except FileNotFoundError:
        return 0

def save_accnum(value):
    with open('accnum.txt', 'w') as file:
        file.write(str(value))



# create a function which is used when the user chooses option 1 to sign up for an account
def customer_register():
    print('Please fill in the following registration form with accuracy for a staff member to insert in the system.')
    accnum = get_accnum() + 1
    save_accnum(accnum)

    # Use the updated account number for filenames
    balance_filename = f'balance_{accnum}.txt'
    transaction_filename = f'transaction_history_{accnum}.txt'
    customer_details_filename = f'customer_details_{accnum}.txt'

    # Create initial balance file if it doesn't exist
    with open(balance_filename, 'a+') as balance_file:
        # Check if the file is empty and write initial balance if needed
        if balance_file.read().strip() == '':
            balance_file.write('0.0')

    customer_details = open('customer_details.txt','a+')

    name = str(input('Enter your full name: '))
    while len(name) == 0:
        print('Error! Please enter your name:')
        name = str(input('Enter your full name: '))
    print('your name is:', name)
    print('-------------------------------')

    gender = str(input('Enter your gender (Male/Female): '))
    while len(gender) == 0:
        print('Error! Please enter your gender:')
        gender = str(input('Enter your gender(Male/Female): '))
    print('your gender is:', gender)
    print('-------------------------------')

    birth = str(input('Enter your date of birth: '))
    while len(birth) == 0:
        print('Error! Please enter your date of birth:')
        birth = str(input('Enter your date of birth: '))
    print('your birthday is:', birth)
    print('-------------------------------')

    occupation = str(input('Enter your current occupation: '))
    while len(occupation) == 0:
        print('Error! Please enter your occupation:')
        occupation = str(input('Enter your current occupation: '))
    print('your occupation is:', occupation)
    print('-------------------------------')

    address = str(input('Enter your address: '))
    while len(address) == 0:
        print('Error! Please enter your address:')
        address = str(input('Enter your address: '))
    print('your address is:', address)


    print('-------------------------------')
    print('1. Saving account')
    print('2. Current account')
    saving = 'Saving account'
    current = 'Current account'
    account = int(input('Enter your preferred account type: '))
    while account != 1 and account!=2:
        print('Error! Please enter your preferred account type::')
        print('1. Saving account')
        print('2. Current account')
        account = int(input('Enter your preferred account type:'))
    if account == 1:
        account = saving
        print('your account is a',account)
        print('-------------------------------')
    elif account == 2:
        account = current
        print('your account is a',account)
        print('-------------------------------')

    accpass = name[0] + name[-1] + str(accnum) + occupation[-1] + address[0] + birth[0] + occupation[-1] + '!'




#printing the customer details into the customer details text file
    customer_details.write(f'Customer Account Number: {accnum}, Customer Account Name: {name}, Customer Birthdate: {birth},'
                           f' Customer\'s occupation: {occupation}, Customer\'s address: {address}, Account Type: {account}, Customer\'s Password: {accpass} \n')
    customer_details.write('-------------------------------\n')
    with open(transaction_filename, 'a+') as transaction_history:
        transaction_history.write(f'Customer {accnum} transaction log:\n')

    customer_details.close()
    print('your account number is:',accnum)
    print('-------------------------------')
    print('your default account password is:',accpass)
    print('Please change your password for added security')


#loging in to a customer account
#def login():
 #   login_id = int(input('Enter your account number: '))
  #  login_pass = str(input('Enter your account password: '))

   # if login_id == get_accnum() and login_pass == accpass:
    #    print('Login successful! Please choose an option from the menu:')




def customer_options():
    print('-------------------------------')
    print('Login Succeful!')
    print('Please choose an option from the following: ')
    print('1 - Deposit Money')
    print('2 - Withdraw Money')
    print('3 - Check Balance')
    print('4 - Generate Account Statement')
    print('5 - Change Password')
    print('6 - Quit')

def login():
    print('-------------------------------')
    found = False

    while not found:
        login_id = input('Enter your account number: ')
        login_pass = str(input('Enter your account password: '))

        customer_details = open('customer_details.txt', 'r')

        # find and read the account number and password from every line on the text file
        for line in customer_details:
            # convert the string into a list by splitting
            acc_info = line.split(',')

            # check if the line has enough elements
            if len(acc_info) >= 2:
                acc_num_str = acc_info[0].split(':')[1].strip()
                acc_pass_str = acc_info[-1].split(':')[1].strip()

                # Converting account number to integer for comparison
                acc_num = int(acc_num_str)

                # Check if the entered credentials match any in the file
                if login_id == acc_num_str and login_pass == acc_pass_str:
                    found = True
                    break

        customer_details.close()

        if not found:
            print('Login failed. Please check your account number and password.')

    customer_options()

def deposit_cash():
    # Get the account number from the user
    accnum = int(input('Enter your account number: '))

    # Use the account number for filenames
    balance_filename = f'balance_{accnum}.txt'
    transaction_filename = f'transaction_history_{accnum}.txt'

    # Open balance file in read mode to get the current balance
    with open(balance_filename, 'r') as balance_file:
        # Read the current balance from the file
        current_balance_str = balance_file.readline().strip()

        # Check if the string is not empty and represents a valid float
        if current_balance_str:
            try:
                current_balance = float(current_balance_str)
            except ValueError:
                # Handle the case where the file contains a non-numeric value
                print("Error: Invalid format in balance file.")
                return
        else:
            # Set a default balance if the file is empty or contains an empty string
            current_balance = 0

    # Get the current date and time
    transaction_datetime = datetime.datetime.now().strftime('%d-%m-%Y')
    # Get the deposit amount from the user
    dep_amount = float(input('Enter deposit amount RM '))

    # Calculate the new balance
    new_balance = current_balance + dep_amount

    # Open balance file in write mode to update the balance
    with open(balance_filename, 'w') as balance_file:
        balance_file.write(str(new_balance))

    # Open transaction history file in append mode to record the transaction
    with open(transaction_filename, 'a+') as transaction_history:
        transaction_history.write(f'{transaction_datetime}: Deposit of: {dep_amount}\n')

    print(f'{dep_amount} RM has been deposited into your account successfully.')

def withdraw_cash():
    # Get the account number from the user
    accnum = int(input('Enter your account number: '))

    # Use the account number for filenames
    balance_filename = f'balance_{accnum}.txt'
    transaction_filename = f'transaction_history_{accnum}.txt'

    # Open balance file in read mode to get the current balance
    try:
        with open(balance_filename, 'r') as balance_file:
            # Read the current balance from the file
            current_balance_str = balance_file.readline().strip()

            # Check if the string is not empty and represents a valid float
            if current_balance_str:
                try:
                    current_balance = float(current_balance_str)
                except ValueError:
                    # Handle the case where the file contains a non-numeric value
                    print("Error: Invalid format in balance file.")
                    return
            else:
                # Set a default balance if the file is empty or contains an empty string
                current_balance = 0
    except FileNotFoundError:
        print(f"Error: Account {accnum} not found.")
        return

    # Get the account type from the user
    account_type = input('Enter your account type (Savings/Current): ').lower()

    # Define the minimum balance based on account type
    if account_type == 'savings':
        min_balance = 100.0
    elif account_type == 'current':
        min_balance = 500.0
    else:
        print("Error: Invalid account type.")
        return

    # Get the withdrawal amount from the user
    withdraw_amount = float(input('Enter withdrawal amount RM '))

    # Check if the withdrawal exceeds the minimum balance
    if current_balance - withdraw_amount < min_balance:
        print(f"Error: Withdrawal amount exceeds minimum balance for {account_type} account.")
        return

    # Calculate the new balance after withdrawal
    new_balance = current_balance - withdraw_amount

    # Get the current date and time
    transaction_datetime = datetime.datetime.now().strftime('%d-%m-%Y')

    # Open balance file in write mode to update the balance
    with open(balance_filename, 'w') as balance_file:
        balance_file.write(str(new_balance))

    # Open transaction history file in append mode to record the transaction
    with open(transaction_filename, 'a+') as transaction_history:
        transaction_history.write(f'{transaction_datetime}: Withdrawal of: {withdraw_amount}\n')

    print(f'{withdraw_amount} RM has been withdrawn from your account successfully.')

def check_balance():
    # Get the account number from the user
    accnum = int(input('Enter your account number: '))

    # Use the account number for filenames
    balance_filename = f'balance_{accnum}.txt'

    try:
        # Open balance file in read mode to get the current balance
        with open(balance_filename, 'r') as balance_file:
            # Read the current balance from the file
            current_balance_str = balance_file.readline().strip()

            # Check if the string is not empty and represents a valid float
            if current_balance_str:
                try:
                    current_balance = float(current_balance_str)
                except ValueError:
                    # Handle the case where the file contains a non-numeric value
                    print("Error: Invalid format in balance file.")
                    return
            else:
                # Set a default balance if the file is empty or contains an empty string
                current_balance = 0

        print(f'Your current account balance is: RM {current_balance}')
    except FileNotFoundError:
        print(f"Error: Account {accnum} not found.")

def generate_statement():
    accnum = int(input('Enter your account number: '))

    # Use the account number for the transaction history filename
    transaction_filename = f'transaction_history_{accnum}.txt'

    try:
        # Open transaction history file in read mode to retrieve transactions
        with open(transaction_filename, 'r') as transaction_history:
            # Get the start and end dates from the user
            start_date = input('Enter the start date (DD-MM-YYYY): ')
            end_date = input('Enter the end date (DD-MM-YYYY): ')

            # Initialize variables to keep track of total deposits and withdrawals
            total_deposits = 0.0
            total_withdrawals = 0.0

            # Initialize variables to keep track of the number of deposits and withdrawals
            num_deposits = 0
            num_withdrawals = 0

            # Iterate through each line in the transaction history file
            for line in transaction_history:
                # Extract the transaction date from the line
                transaction_date_str = line.split(':')[0].strip()

                # Check if the transaction date is within the specified range
                if start_date <= transaction_date_str <= end_date:
                    print(line.strip())  # Print the transaction details

                    # Extract the transaction amount from the line
                    transaction_amount_str = line.split(':')[-1].strip()
                    transaction_amount = float(transaction_amount_str)

                    # Update total deposits or withdrawals based on the transaction type
                    if 'Deposit' in line:
                        total_deposits += transaction_amount
                        num_deposits += 1
                    elif 'Withdrawal' in line:
                        total_withdrawals += transaction_amount
                        num_withdrawals += 1

            # Print the total deposits, withdrawals, and the number of each
            print(f'Total Deposits: {total_deposits} RM')
            print(f'Total Withdrawals: {total_withdrawals} RM')
            print(f'Total Number of Deposits: {num_deposits}')
            print(f'Total Number of Withdrawals: {num_withdrawals}')

    except FileNotFoundError:
        print(f"Error: Account {accnum} not found.")



def change_password():
    print('-------------------------------')
    accnum = int(input('Please enter your account number: '))
    check_current_pass = str(input('Please enter your current password: '))

    with open('customer_details.txt', 'r') as customer_details:
        lines = customer_details.readlines()

    found = False
    for line in lines:
        # Extract account number from the line
        acc_data_start = line.find('Account Number:') + len('Account Number:')
        acc_data_end = line.find(',', acc_data_start)

        if acc_data_end == -1:
            continue

        accnum_str = line[acc_data_start:acc_data_end].strip()

        # Check if accnum_str is a valid integer
        if not accnum_str.isdigit():
            continue

        try:
            current_accnum = int(accnum_str)
        except ValueError:
            continue

        if current_accnum == accnum:
            # Extract password from the line
            pass_data_start = line.find('Password:') + len('Password:')
            accpass = line[pass_data_start:].strip()
            found = True
            break

    if not found:
        print('Account number not found.')
        return

    if check_current_pass == accpass:
        new_acc_pass = str(input('Please enter your new password: '))
        while len(new_acc_pass) < 8:
            print('Error! Your new password needs to be made of at least 8 characters.')
            new_acc_pass = str(input('Please enter your new password: '))

        # Update the password in the list
        for i, line in enumerate(lines):
            current_accnum_str = line[acc_data_start:acc_data_end].strip()

            # Check if current_accnum_str is a valid integer
            if not current_accnum_str.isdigit():
                continue

            current_accnum = int(current_accnum_str)

            if current_accnum == accnum:
                lines[i] = line[:pass_data_start] + f' {new_acc_pass}\n'
                break

        # Write the updated list back to the file
        with open('customer_details.txt', 'w') as customer_details:
            customer_details.writelines(lines)
        print('Password changed successfully!')
    else:
        print('Incorrect current password.')







# this is what the customer inputs as soon as he is presented with the customer menu of signing up or logging in
print('-------------------------------')
customer_choice = int(input('Enter your choice of action: '))
print('You chose:', customer_choice)

if customer_choice == 1:
    print('-------------------------------')
    customer_register()
    customer_options()  # Present the customer options menu after registration
elif customer_choice == 2:
    login()
elif customer_choice == 3:
    print('Thank You for using our services.')
    exit()

while customer_choice not in [1, 2, 3]:
    print('-------------------------------')
    print('Error! Please choose an option from the menu: ')
    customer_choice = int(input('Enter your choice of action: '))
    print('You chose:', customer_choice)
    if customer_choice == 1:
        print('-------------------------------')
        customer_register()
        customer_options()  # Present the customer options menu after registration
    elif customer_choice == 2:
        login()
    elif customer_choice == 3:
        print('Thank You for using our services.')
        exit()



#error here that needs fixing the error messes up with the customer inital menu where they choose to sign up/login


print('-------------------------------')
customer_menu_choice = input('Please enter your preferred option from the menu: ')
print('you chose:', customer_menu_choice)

if customer_menu_choice == '1':
    print('-------------------------------')
    deposit_cash()
elif customer_menu_choice == '2':
    withdraw_cash()
elif customer_menu_choice == '3':
    check_balance()
elif customer_menu_choice == '4':
    generate_statement()
elif customer_menu_choice == '5':
    change_password()
elif customer_menu_choice == '6':
    print('Thank You for using our services.')
    exit()

while customer_menu_choice not in ['1', '2', '3', '4', '5', '6']:
    print('-------------------------------')
    print('Error! Please choose an option from the menu: ')
    customer_menu_choice = input('Enter your choice of action: ')
    print('You chose:', customer_menu_choice)
    if customer_menu_choice == '1':
        print('-------------------------------')
        deposit_cash()
    elif customer_menu_choice == '2':
        withdraw_cash()
    elif customer_menu_choice == '3':
        check_balance()
    elif customer_menu_choice == '4':
        generate_statement()
    elif customer_menu_choice == '5':
        change_password()
    elif customer_menu_choice == '6':
        print('Thank You for using our services.')
        exit()



