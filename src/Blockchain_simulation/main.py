import hashlib
import time

DIFFICULTY = 4

def get_fake_transaction():
    return f"Transaction at {time.time()}"

def calculate_hash(data, previous_hash, nonce):
    content = data + str(previous_hash) + str(nonce)
    return hashlib.sha256(content.encode()).hexdigest()

def mine_block(data,previous_hash):
    nonce = 0
    while True:
        hash_result = calculate_hash(data, previous_hash, nonce)
        if hash_result.startswith("0" * DIFFICULTY):
            print(f"Block Mined! Nonce: {nonce}, Hash: {hash_result}")
            return nonce, hash_result
        nonce += 1

def create_block(data, previous_hash, chain):
    nonce, current_hash = mine_block(data, previous_hash)
    block = {
        "data": data,
        "previous_hash": previous_hash,
        "nonce": nonce,
        "hash": current_hash
    }
    chain.append(block)
    return current_hash

blockchain = []

data = input("Add optional message (or press Enter to skip): ")
if not data:
    data = get_fake_transaction()
    
previous_hash = "0"
previous_hash = create_block(data, previous_hash, blockchain)

while True:
    choice = int(input("Press 1 to add a new block, 2 to finish: "))
    if choice != 1:
        break
    data = input("Add optional message (or press Enter to skip): ")
    if not data:
        data = get_fake_transaction()
        
    previous_hash = create_block(data, previous_hash, blockchain)

for i, block in enumerate(blockchain):
    if i == 0:
        print("\n=== Genesis Block ===")
    else:
        print(f"\n=== Block {i} ===")
    print(f"Data: {block['data']}")
    print(f"Previous Hash: {block['previous_hash']}")
    print(f"Nonce: {block['nonce']}")
    print(f"Hash: {block['hash']}")