import hashlib

file = input("Specify file path: ")
stored_hash_path = input("Specify the stored hash file path: ")

with open(file, 'rb') as f:
    content = f.read()
    true_hash = hashlib.sha256(content).hexdigest()

with open(stored_hash_path, 'r') as h:
    test_hash = h.read().strip()

if test_hash == true_hash:
    print("File has not been altered. File integrity successful.")
else:
    print("File has been altered. File integrity failed.")