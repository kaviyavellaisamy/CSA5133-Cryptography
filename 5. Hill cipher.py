import numpy as np

text = input("Enter text: ").replace(" ", "").upper()
choice = input("Enter E for Encryption or D: ").lower()

key = np.array([[3, 3],
                [2, 5]])

if len(text) % 2 != 0:
    text += 'X'

result = ""

# Encryption
if choice == 'e':
    for i in range(0, len(text), 2):
        pair = np.array([[ord(text[i]) - 65],
                         [ord(text[i+1]) - 65]])
        cipher = np.dot(key, pair) % 26
        result += chr(cipher[0][0] + 65) + chr(cipher[1][0] + 65)

# Decryption
elif choice == 'd':
    inv_key = np.array([[15, 17],
                        [20, 9]])   # Inverse of key matrix mod 26
    for i in range(0, len(text), 2):
        pair = np.array([[ord(text[i]) - 65],
                         [ord(text[i+1]) - 65]])
        plain = np.dot(inv_key, pair) % 26
        result += chr(plain[0][0] + 65) + chr(plain[1][0] + 65)

print("Result:", result)
