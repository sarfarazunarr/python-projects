import random 

characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*_"

while True:
    password_length = int(input('Enter the length of password  '))
    password_count = int(input('How many passwords do you want  '))

    for i in range(0, password_count):
        password = ''
        for j in range(0, password_length):
            pass_char = random.choice(characters)
            password = password + pass_char
        print('Here is your password', password)
    repeat= input('Do you wants to generate another passwords?(Y/N)').lower()
    if repeat == 'n' :
        break

print('Thanks for using password generator!')
    
