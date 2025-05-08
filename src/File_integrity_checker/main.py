import hashlib
import json
from pathlib import Path

def hash_file(filepath):
    hasher = hashlib.sha256()
    with open(filepath, 'rb') as f:
        while True:
            chunk = f.read(8192)
            if not chunk:
                break
            hasher.update(chunk)
    return hasher.hexdigest()

def hash_all_files(directory):
    directory = Path(directory)
    return {str(f): hash_file(f) for f in directory.glob("*") if f.is_file()}

def save_hashes(hash_dict, store_file):
    with open(store_file, 'w') as f:
        json.dump(hash_dict, f, indent=4)

def load_previous_hashes(store_file):
    try:
        with open(store_file, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def compare_hashes(old_hashes, new_hashes):
    old_files = set(old_hashes)
    new_files = set(new_hashes)

    added = new_files - old_files
    removed = old_files - new_files
    changed = {f for f in old_files & new_files if old_hashes[f] != new_hashes[f]}

    return added, removed, changed

if __name__ == "__main__":
    dump = "file_hashes.json"
    print("Do you want to hash a file/directory or check the integrity?")
    choice = int(input("Press 1 for hash and 2 for check: "))

    if choice == 1:
        choice2 = int(input("Do you want to hash:\n1. A single file\n2. All contents of a directory\nEnter choice: "))
        if choice2 == 1:
            filepath = input("Specify the file path: ")
            content = {filepath: hash_file(filepath)}
            save_hashes(content, dump)
        else:
            directorypath = input("Specify the directory path: ")
            dir_content = hash_all_files(directorypath)
            save_hashes(dir_content, dump)

    elif choice == 2:
        choice2 = int(input("Do you want to check:\n1. A single file\n2. All contents of a directory\nEnter choice: "))
        old_hashes = load_previous_hashes(dump)
        if choice2 == 1:
            filepath = input("Specify the file path: ")
            new_hashes = {filepath: hash_file(filepath)}
        else:
            directorypath = input("Specify the directory path: ")
            new_hashes = hash_all_files(directorypath)

        added, removed, changed = compare_hashes(old_hashes, new_hashes)
        print("Added files:", added)
        print("Removed files:", removed)
        print("Changed files:", changed)