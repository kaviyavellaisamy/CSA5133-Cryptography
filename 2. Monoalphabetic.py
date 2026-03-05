plain = "abcdefghijklmnopqrstuvwxyz"
cipher = "qwertyuiopasdfghjklzxcvbnm"

choice = input("Enter E for Encryption or D for Decryption: ").upper()
text = input("Enter text: ").lower()

result = ""

if choice == "E":   
    for ch in text:
        if ch in plain:
            result += cipher[plain.index(ch)]
        else:
            result += ch
    print("Encrypted text:", result)

elif choice == "D":   
    for ch in text:
        if ch in cipher:
            result += plain[cipher.index(ch)]
        else:
            result += ch
    print("Decrypted text:", result)

else:
    print("Invalid choice")
