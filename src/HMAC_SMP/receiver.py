import hmac
import hashlib

SECRET_KEY = b'blablabla blebleble blublublu'

def create_hmac(message : str, key : bytes) -> str:
    return hmac.new(key, message.encode(), hashlib.sha256).hexdigest()

def verify_message(packet: str, key: bytes) -> bool:

    lines = packet.strip().split('\n')
    message = lines[0].split(': ', 1)[1].strip()
    received_hmac = lines[1].split(': ', 1)[1].strip()
    expected_hmac = create_hmac(message, key)

    return hmac.compare_digest(received_hmac, expected_hmac)

with open('src/HMAC_SMP/packet.txt', 'r') as f:
    packet_data = f.read()
result = verify_message(packet_data,SECRET_KEY)

if result is True:
    print("Results match the code hasn't been tampered")
else:
    print("HMACs do not match")


