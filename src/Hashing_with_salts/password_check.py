import bcrypt

def encrypting_passwrd(password,salt):
    hashed = bcrypt.hashpw(password.encode(), salt)
    return hashed

file = "password_storage.txt"

with open(file, "r") as f:
    lines = f.readlines()
    
    stored_hashed = lines[0].split(": ")[1].strip().encode()
    stored_salt = lines[1].split(": ")[1].strip().encode()
    
password = input("Give password : ")
new_hash = encrypting_passwrd(password,stored_salt)

if new_hash == stored_hashed:
    print("Password Correct")
else:
    print("Password invalid")
