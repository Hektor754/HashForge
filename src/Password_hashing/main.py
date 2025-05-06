import os
import hashlib

password = input("Enter your password: ")
salt = os.urandom(16)

salted_password = salt + password
hashed = hashlib.pbkdf2_hmac('sha_256', password, salt, 100_000)

with open('store_password.txt', 'x+') as f:
    f.write(f"Used Salt : {salt.hex()}")
    f.write(f"Hashed password : {hashed.hex()}")
    f.seek(0)