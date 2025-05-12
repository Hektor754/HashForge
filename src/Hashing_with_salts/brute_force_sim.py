import bcrypt

file = "src/Hashing_with_salts/password_storage.txt"

# Reading the stored hash and salt
with open(file, 'r') as f:
    lines = f.readlines()
    
    stored_hashed = lines[0].split(": ")[1].strip().encode()
    stored_salt = lines[1].split(": ")[1].strip().encode()
    
possible_passwords = ["password", "password123", "letmein", "12345qwert", "admin", "user", "user123"]

# This function demonstrates that without knowing the salt, brute force is impossible
def brute_force_attack_rsalt(possible_passwords):
    print("\n Brute Force without Known Salt (Random Salt Each Time):")
    for guess in possible_passwords:
        print(f"Trying password: {guess}")
        # Random salt each time (This makes it impossible to match)
        hashed_guess = bcrypt.hashpw(guess.encode(), bcrypt.gensalt())
        if hashed_guess == stored_hashed:
            print(f"✅ Password Found: {guess}")
            return guess
    print(" Password not found (Random Salt makes it impossible).")
    return None

# This function demonstrates that if you know the salt, you can brute force the password
def brute_force_attack_withsalt(possible_passwords, stored_salt):
    print("\n Brute Force with Known Salt:")
    for guess in possible_passwords:
        print(f"Trying password: {guess}")
        # Using the known stored salt
        hashed_guess = bcrypt.hashpw(guess.encode(), stored_salt)
        if hashed_guess == stored_hashed:
            print(f" Password Found: {guess}")
            return guess
    print(" Password not found (even with known salt).")
    return None

# Running both brute force attacks
guess = brute_force_attack_rsalt(possible_passwords)
guess2 = brute_force_attack_withsalt(possible_passwords, stored_salt)

# Outputting results clearly
if guess is not None:
    print(f"\n The password (found without knowing the salt) is: {guess}")
else:
    print("\n Brute force without knowing the salt failed.")

if guess2 is not None:
    print(f"\n The password (found using the known salt) is: {guess2}")
else:
    print("\n Brute force with known salt failed.")