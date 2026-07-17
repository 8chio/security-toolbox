import random

def generate_password(length):
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+"
    password = ""
    for i in range(length):
        password = password + random.choice(letters)
    return password