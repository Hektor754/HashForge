

file = "password_storage.txt"

with open(file, "r") as f:
    lines = f.readlines()
    
    stored_hashed = lines[0].split(": ")[1].strip()
    stored_salt = lines[0].split(": ")[1].strip()