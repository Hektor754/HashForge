import bcrypt

def encrypting_passwrd(password):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode(), salt)
    return hashed, salt

password = input("Give a password: ")
hashed, salt = encrypting_passwrd(password)

with open("password_storage.txt", 'w+') as f:
    f.write(f"Hash: {hashed.decode()}\n")
    f.write(f"Salt: {salt.decode()}\n")