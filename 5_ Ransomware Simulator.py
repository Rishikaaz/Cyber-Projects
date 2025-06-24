from cryptography.fernet import Fernet
import os

key = Fernet.generate_key()
cipher = Fernet(key)

def encrypt_file(file_path):
    with open(file_path, 'rb') as f:
        data = f.read()
    with open(file_path, 'wb') as f:
        f.write(cipher.encrypt(data))

# Encrypt all .txt files in a folder
folder = "sample_folder"
for file in os.listdir(folder):
    if file.endswith(".txt"):
        encrypt_file(os.path.join(folder, file))

print("Files encrypted. Save this key to decrypt:\n", key.decode())
