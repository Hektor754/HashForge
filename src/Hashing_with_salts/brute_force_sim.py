import bcrypt

file = "src/Hashing_with_salts/password_storage.txt"

with open(file, 'r') as f:
    lines = f.readlines()
    
    stored_hashed = lines[0].split(": ")[1].strip().encode()
    stored_salt = lines[1].split(": ")[1].strip().encode()
    
possible_password = ["password", "password123", "letmein", "12345qwert", "admin", "user", "user123"]

def brute_force_attack_rsalt(possible_password):
    for guess in possible_password:
        print(f"Trying password : {guess}")
        hashed_guess = bcrypt.hashpw(guess.encode(), bcrypt.gensalt())
        if hashed_guess == stored_hashed:
            print("Password Found")
            return guess
        else:
            print("Password not found")
    return None

guess = brute_force_attack_rsalt(possible_password)
if guess is not None:
    print(f"The password is : {guess}")