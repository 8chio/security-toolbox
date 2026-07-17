import random

print("=== Password Generator ===")
length = int(input("Enter the desired password length: "))

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+"

password = ""

for i in range(length):
    password = password + random.choice(letters)

print(password)