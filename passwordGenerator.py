import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
           'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
           'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '~', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '+']
print('Welcome to the Password Generator!')
nr_latters=int(input('How many latters would you link in your password?\n'))
nr_symbels=int(input('How many symbols would you link?\n'))
nr_numbers=int(input('How many numbers would you link?\n'))
password_list = []
for i in range(1, nr_latters+1):
    password_list+= random.choice(letters)
for i in range(1, nr_symbels+1):
    password_list+= random.choice(symbols)
for i in range(1, nr_numbers+1):
    password_list+= random.choice(numbers)
random.shuffle(password_list)
password = ''
for char in password_list:
    password+=char
print(f"your password is {password}")
