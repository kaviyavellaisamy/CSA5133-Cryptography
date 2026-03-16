from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP, AES
from Crypto.Random import get_random_bytes

key = RSA.generate(2048)
public_key = key.publickey()
private_key = key

print("Public Key Generated")
print("Private Key Generated")

message = input("Enter the message: ").encode()

session_key = get_random_bytes(16)

cipher_rsa = PKCS1_OAEP.new(public_key)
encrypted_session_key = cipher_rsa.encrypt(session_key)

cipher_aes = AES.new(session_key, AES.MODE_EAX)
ciphertext, tag = cipher_aes.encrypt_and_digest(message)

print("\nEncrypted Message:", ciphertext)

cipher_rsa = PKCS1_OAEP.new(private_key)
decrypted_session_key = cipher_rsa.decrypt(encrypted_session_key)

cipher_aes = AES.new(decrypted_session_key, AES.MODE_EAX, cipher_aes.nonce)
decrypted_message = cipher_aes.decrypt(ciphertext)

print("\nDecrypted Message:", decrypted_message.decode())
