from cryptography.fernet import Fernet
import os


# Below function will write key
def writeKey():
    key = Fernet.generate_key()
    with open('key.key', 'wb') as key_file:
        key_file.write(key)

#This function will load key
def loadKey():
    if not os.path.isfile('key.key'):
        writeKey()

    with open('key.key', 'rb') as key_file:
        key = key_file.read()
        return key

# Take master password
def enter_master_password():
    master_pwd = input("Please enter your master password: ")
    return master_pwd

# Check is new user or old and verify password
def check_master_password():
    if not os.path.isfile('master_password.txt'):
        print("Welcome! You are a new user. Please create a master password to continue.")
        master_pwd = input("Create a master password: ")

        key = loadKey()
        fer = Fernet(key)
        encrypted_master_pwd = fer.encrypt(master_pwd.encode())

        with open('master_password.txt', 'wb') as mp_file:
            mp_file.write(encrypted_master_pwd)

        return master_pwd
    else:
        print("Enter your existing master password to continue.")
        entered_master_pwd = enter_master_password()

        with open('master_password.txt', 'rb') as mp_file:
            encrypted_master_pwd = mp_file.read()

        key = loadKey()
        fer = Fernet(key)
        decrypted_master_pwd = fer.decrypt(encrypted_master_pwd).decode()

        while entered_master_pwd != decrypted_master_pwd:
            print("Incorrect password. Please try again.")
            entered_master_pwd = enter_master_password()

        return decrypted_master_pwd

# View all saved Password
def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            site, user, pwd = data.split(' || ')
            print('Sitename: ' + site + ' Username: ' + user +
                  ' Password: ' + fer.decrypt(pwd.encode()).decode())

# Add new password
def add():
    account = input(
        'Enter account or sitename where you will use your password? ')
    username = input('Enter your username: ')
    password = input('Enter secret password ')

    encrypted_password = fer.encrypt(password.encode())
    with open('passwords.txt', 'a') as f:
        f.write(account + " || " + username + " || " +
                encrypted_password.decode() + "\n")
    print('Password Saved')

# Call functions
master_pwd = check_master_password()
key = loadKey()
key += master_pwd.encode()
fer = Fernet(key)

# Taking input to perform actions
while True:
    mode = input(
        'Please select mode for adding or deleting password (view / add / q to quit): ').lower()

    if mode == 'q':
        break

    elif mode == 'view':
        view()
    elif mode == 'add':
        add()
    else:
        print('Invalid mode')
        continue


# (View info.txt) You can add more features based on your requirements. Good Luck!
