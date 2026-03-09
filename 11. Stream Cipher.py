def stream_cipher(text, key):
    result = ""

    for i in range(len(text)):
        k = key[i % len(key)]           # repeat key
        result += chr(ord(text[i]) ^ ord(k))  # XOR operation

    return result


choice = input("Enter E for Encryption or D for Decryption: ").upper()
text = input("Enter text: ")
key = input("Enter key: ")

output = stream_cipher(text, key)

print("Result:", output)
