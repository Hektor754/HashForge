from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.backends import default_backend
from cryptography.exceptions import InvalidSignature

public_file = "src/Hashed_signatures/public_key.pem"
with open(public_file, 'rb') as key_file:
    public_key = serialization.load_pem_public_key(
        key_file.read(),
        backend=default_backend()
    )

msg_file = "src/Hashed_signatures/test_message.txt"

with open(msg_file, 'r') as msg:
    content = msg.read()

    if "---BEGIN SIGNATURE---" in content and "---END SIGNATURE---" in content:
        message_part = content.split("---BEGIN SIGNATURE---")[0].strip()
        signature_part = content.split("---BEGIN SIGNATURE---")[1].split("---END SIGNATURE---")[0].strip()
    else:
        print("Signature not found in the message file.")
        exit()

    signature_bytes = bytes.fromhex(signature_part.replace("\n", ""))

try:
    public_key.verify(
        signature_bytes,
        message_part.encode(),
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    print("The signature is VALID. Message integrity and authenticity are verified.")
except InvalidSignature:
    print("The signature is INVALID. The message may have been tampered with.")