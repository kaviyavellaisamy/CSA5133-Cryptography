from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

key = RSA.generate(2048)
public_key = key.publickey()
private_key = key

message = input("Enter the email message: ").encode()

cipher = PKCS1_OAEP.new(public_key)
encrypted_message = cipher.encrypt(message)

print("\nEncrypted Email Message:")
print(encrypted_message)

cipher = PKCS1_OAEP.new(private_key)
decrypted_message = cipher.decrypt(encrypted_message)

print("\nDecrypted Email Message:")
print(decrypted_message.decode())
