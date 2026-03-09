def rotl(x, y, w):
    return ((x << y) & (2**w - 1)) | (x >> (w - y))

def rotr(x, y, w):
    return (x >> y) | ((x << (w - y)) & (2**w - 1))


choice = int(input("Enter choice (1 Encrypt / 2 Decrypt): "))

if choice == 1:
    text = input("Enter text: ")
elif choice == 2:
    text = bytes.fromhex(input("Enter encrypted text: ")).decode()
else:
    print("Invalid choice")
    exit()

key = int(input("Enter key: "))
rounds = int(input("Enter rounds: "))
w = int(input("Enter word size: "))

result = ""

for ch in text:
    x = ord(ch)

    if choice == 1:  # Encryption
        for i in range(rounds):
            x = rotl(x ^ key, key % w, w)

    elif choice == 2:  # Decryption
        for i in range(rounds):
            x = rotr(x, key % w, w) ^ key

    result += chr(x)

if choice == 1:
    print("Encrypted Text:", result.encode().hex())
else:
    print("Decrypted Text:", result)
