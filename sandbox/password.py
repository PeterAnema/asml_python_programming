import random

required_length = 8
n_lowercase = 1
n_uppercase = 1
n_numbers = 1
n_special = 1

lowercase = 'abcdefghijklmnopqrstuvwxyz'
uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
special = '@#$%&*+?!'

characters = []
characters += random.choices(lowercase, k=n_lowercase)
characters += random.choices(uppercase, k=n_uppercase)
characters += random.choices(numbers, k=n_numbers)
characters += random.choices(special, k=n_special)
characters += random.choices(lowercase + uppercase + numbers,
                             k = required_length - n_lowercase - n_uppercase - n_numbers - n_special)

random.shuffle(characters)

password = ''.join(characters)

print('New password: ', password)
