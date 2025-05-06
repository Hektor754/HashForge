import hashlib

file = 'store_password.txt'
with open(file, "r") as f:
    lines = f.readlines()
    salt_hex = lines[0].split(":")[1].strip()
    hash_hex = lines[1].split(":")[1].strip()
    
salt = bytes.fromhex(salt_hex)
stored_hash = bytes.fromhex(hash_hex)

user_password = input("Give password : ")
new_hash = hashlib.pbkdf2_hmac('sha256', user_password, salt, 100_000)

if new_hash == stored_hash:
    print("Password is correct")
else:
    print("Incorrect password")
