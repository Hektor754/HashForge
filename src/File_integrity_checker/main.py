import hashlib

file = input("Specify file path: ")

with open(file, 'rb') as f:
    content = f.read()
    hashed_file = hashlib.sha256(content).hexdigest()

with open('stored_hashedfile.txt', 'w') as h:
    h.write(hashed_file)

print("Hash stored successfully.")
