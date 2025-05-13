import hashlib
import csv
from pathlib import Path
import pandas as pd
import os

def hash_file(file_path):
    hasher = hashlib.sha256()
    try:
        with open(file_path, 'rb') as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hasher.update(chunk)
        return hasher.hexdigest()
    except PermissionError:
        return None

def write_hashes_to_csv(root_directory, output_csv):
    existing_data = pd.read_csv(output_csv) if os.path.exists(output_csv) else pd.DataFrame(columns=['Directory', 'File Name', 'File Hash'])
    
    with open(output_csv, mode='a', newline='') as file:
        writer = csv.writer(file)
        if existing_data.empty:
            writer.writerow(['Directory', 'File Name', 'File Hash'])
        
        for item in root_directory.rglob('*'):
            if item.is_file():
                file_hash = hash_file(item)
                if file_hash:
                    if not ((existing_data['Directory'] == str(item.parent)) & 
                            (existing_data['File Name'] == item.name) & 
                            (existing_data['File Hash'] == file_hash)).any():
                        writer.writerow([item.parent, item.name, file_hash])

root_directory = Path(input("Specify the directory path you want it to start"))
output_csv = 'file_hashes.csv'
write_hashes_to_csv(root_directory, output_csv)

data = pd.read_csv('file_hashes.csv')

duplicate_hashes = data[data.duplicated(subset=['File Hash'], keep=False)]

hashes_to_delete = list(duplicate_hashes['File Hash'].unique())

for hash_value in hashes_to_delete:
    matches = data[data["File Hash"] == hash_value]
    for _, row in matches.iloc[1:].iterrows():
        file_path = os.path.join(row['Directory'], row['File Name'])
        if os.path.exists(file_path):
            os.remove(file_path)
            print(f"Deleted: {file_path}")