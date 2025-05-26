import hmac
import hashlib

SECRET_KEY = b'blablabla blebleble blublublu'

def create_hmac(message : str, key : bytes) -> str:
    return hmac.new(key, message.encode(), hashlib.sha256).hexdigest()

def send_message(message : str):
    mac = create_hmac(message, SECRET_KEY)
    with open('packet.txt', 'w') as p:
        p.write(f"Message : {message}\nHMAC : {mac}")

message = 'message.txt'
send_message(message)