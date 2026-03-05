text = input("Enter text: ").lower()
key = input("Enter key: ").lower()
choice = input("Enter E for Encryption or D for Decryption: ").lower()

result = ""
key_index = 0

for ch in text:
    if ch.isalpha():
        shift = ord(key[key_index % len(key)]) - 97
        
        if choice == 'e':   # Encryption
            result += chr((ord(ch) - 97 + shift) % 26 + 97)
        elif choice == 'd':  # Decryption
            result += chr((ord(ch) - 97 - shift) % 26 + 97)
        
        key_index += 1
    else:
        result += ch

print("Result:", result)
