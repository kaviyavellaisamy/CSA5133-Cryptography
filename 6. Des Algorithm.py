from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

print("1. Encrypt")
print("2. Decrypt")

choice = input("Enter your choice (1/2): ")
key = input("Enter 8-character key: ")

if len(key) != 8:
    print("Key must be exactly 8 characters!")
    exit()

cipher = DES.new(key.encode(), DES.MODE_ECB)

if choice == "1":
    message = input("Enter message to encrypt: ")
    padded_text = pad(message.encode(), DES.block_size)
    encrypted_text = cipher.encrypt(padded_text)
    print("Encrypted (hex):", encrypted_text.hex())

elif choice == "2":
    encrypted_hex = input("Enter hex value to decrypt: ")
    encrypted_bytes = bytes.fromhex(encrypted_hex)
    decrypted_text = unpad(cipher.decrypt(encrypted_bytes), DES.block_size)
    print("Decrypted message:", decrypted_text.decode())

else:
    print("Invalid choice!")
