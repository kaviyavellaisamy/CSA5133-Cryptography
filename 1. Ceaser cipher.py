text = input("Enter text: ")
shift = int(input("Enter shift value: "))
choice = input("Enter E for Encryption or D for Decryption: ").upper()

result = ""

for ch in text:
    if ch.isalpha():
        if choice == "E":
            result += chr((ord(ch) - 97 + shift) % 26 + 97)
        elif choice == "D":
            result += chr((ord(ch) - 97 - shift) % 26 + 97)
    else:
        result += ch

if choice == "E":
    print("Encrypted text:", result)
elif choice == "D":
    print("Decrypted text:", result)
else:
    print("Invalid choice")
