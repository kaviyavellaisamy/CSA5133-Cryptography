from Crypto.Cipher import Blowfish
from Crypto.Util.Padding import pad, unpad

key = b'secret_k'   # Blowfish key (4–56 bytes)

choice = input("Enter E for Encryption or D for Decryption: ").upper()

if choice == "E":
    text = input("Enter text to encrypt: ")
    
    cipher = Blowfish.new(key, Blowfish.MODE_ECB)
    encrypted = cipher.encrypt(pad(text.encode(), Blowfish.block_size))
    
    print("Encrypted text:", encrypted.hex())

elif choice == "D":
    text = bytes.fromhex(input("Enter encrypted text (hex): "))
    
    cipher = Blowfish.new(key, Blowfish.MODE_ECB)
    decrypted = unpad(cipher.decrypt(text), Blowfish.block_size)
    
    print("Decrypted text:", decrypted.decode())

else:
    print("Invalid choice")
