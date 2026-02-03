import random
import string

numbers = string.digits
symbols= string.punctuation
lowercase_letters= string.ascii_lowercase
uppercase_letters= string.ascii_uppercase
all_characters = [numbers,symbols,lowercase_letters,uppercase_letters]
password=""

for j in range(4):
    for i in range(3):
        password += random.choice(all_characters[j])


password = list(password)

random.shuffle(password)



new_password =""
for i in password:
    new_password += i

print(new_password)