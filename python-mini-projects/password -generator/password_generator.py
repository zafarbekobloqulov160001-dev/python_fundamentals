import random

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%"


password=""
password_length=int(input(" Enter a password_length="))
characters=letters+numbers+symbols
for i in range(password_length):
 password += random.choice(characters)
print("Generate password=",password)