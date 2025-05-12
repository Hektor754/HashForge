from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.backends import default_backend

private_file = "src/Hashed_signatures/private_key.pem"

with open(private_file, 'rb') as key_file:
    private_key = serialization.load_pem_private_key(
        key_file.read(),
        password=None,
        backend=default_backend()
    )

msg_file = "src/Hashed_signatures/test_message.txt"

with open(msg_file, 'r+') as msg:
    content = msg.read()
    signature = private_key.sign(
        content.encode(),
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )

    msg.write("\n\n---BEGIN SIGNATURE---\n")
    signature_hex = signature.hex()
    for i in range(0, len(signature_hex), 64):
        msg.write(signature_hex[i:i+64] + "\n")
    msg.write("\n---END SIGNATURE---")

print("Signature added to the message file.")