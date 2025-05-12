from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.backends import default_backend

private_file = "src/Hashed_signatures/private_key.pem"
with open(private_file, 'rb') as key_file:
    private_key = serialization.load_pem_private_key(
        key_file.read()
        PASSWORD = None
        backend = default_backend()
    )
    
msg_file = "src/Hashed_signatures/test_message.txt"

with open(msg_file, 'r+') as msg:
    content = msg.read()
    hasher = hashes.Hash(hashes.SHA256(), backend = default_backend())
    hasher.update(content)
    hashed_message = hasher.finalize()
    
    signature = private_key.sign(
        hashed_message,
        padding.PSS(
            mgf = padding.MGF1(hashes.SHA256()),
            salt_length = padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )

print("Signature :", signature.hex())