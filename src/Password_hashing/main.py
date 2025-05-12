import os
import hashlib

password = input("Enter your password: ")

hashed = hashlib.pbkdf2_hmac('sha256', password.encode(), 100_000)

with open('store_password.txt', 'w') as f:
    f.write(f"Hashed password : {hashed.hex()}\n")