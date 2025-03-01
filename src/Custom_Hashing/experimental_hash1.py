import random

def hashing(text):

    hash_value = 0x1234567890abcdef1234567890abcdef    
    ascii_values = [ord(char) for char in text]
    
    for i, element in enumerate(ascii_values):
        hash_value ^= (hash_value << 5) + (hash_value >> 2) + element + (i * 31)
        hash_value &= 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF

    random.seed(hash_value)
    hash_value ^= random.getrandbits(128)  
    hash_value &= 0xFFFFFFFFFFFFFFFF  
    return f"{hash_value:016x}"  

print(hashing("world is a mythical place"))


