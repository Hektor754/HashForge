import hashlib

def calculate_hash(data, previous_hash):
    content = data + str(previous_hash)
    return hashlib.sha256(content.encode()).hexdigest()

def create_block(data, previous_hash, chain):
    current_hash = calculate_hash(data, previous_hash)
    block = [data, previous_hash, current_hash]
    chain.append(block)
    return current_hash

blockchain = []

data = input("Write a message to store in a block: ")
previous_hash = "0"
previous_hash = create_block(data, previous_hash, blockchain)

while True:
    choice = int(input("Press 1 to add a new block, 2 to finish: "))
    if choice != 1:
        break
    data = input("Write a message to store in a block: ")
    previous_hash = create_block(data, previous_hash, blockchain)

for i, block in enumerate(blockchain):
    if i == 0:
        print("\n=== Genesis Block ===")
    else:
        print(f"\n=== Block {i} ===")
    print(f"Data: {block[0]}")
    print(f"Previous Hash: {block[1]}")
    print(f"Current Hash: {block[2]}")