# Sender Side
import socket
from Crypto.Cipher import AES
import base64

key = b"1234567890abcdef"  # 16-byte key
cipher = AES.new(key, AES.MODE_EAX)

msg = input("Message: ").encode()
ciphertext, tag = cipher.encrypt_and_digest(msg)

s = socket.socket()
s.connect(("localhost", 9999))
s.send(cipher.nonce + tag + ciphertext)

# Receiver Side
import socket
from Crypto.Cipher import AES

s = socket.socket()
s.bind(("localhost", 9999))
s.listen(1)
conn, _ = s.accept()
data = conn.recv(1024)

nonce, tag, ciphertext = data[:16], data[16:32], data[32:]
key = b"1234567890abcdef"
cipher = AES.new(key, AES.MODE_EAX, nonce)
msg = cipher.decrypt_and_verify(ciphertext, tag)
print("Decrypted:", msg.decode())
