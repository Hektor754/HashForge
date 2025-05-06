import os
import hashlib

password = input("Enter your password: ")
salt = os.urandom(16)

hashed = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100_000)

with open('store_password.txt', 'w') as f:
    f.write(f"Used Salt : {salt.hex()}\n")
    f.write(f"Hashed password : {hashed.hex()}\n")