p = int(input("Enter prime p: "))
q = int(input("Enter prime q: "))

n = p * q
phi = (p - 1) * (q - 1)

e = int(input("Enter public key e: "))
d = int(input("Enter private key d: "))

choice = input("Enter E for Encrypt or D for Decrypt: ").upper()

if choice == 'E':
    msg = input("Enter message: ")
    cipher = [pow(ord(ch), e, n) for ch in msg]
    print("Encrypted:", cipher)

elif choice == 'D':
    cipher = list(map(int, input("Enter encrypted numbers (space separated): ").split()))
    plain = ''.join(chr(pow(ch, d, n)) for ch in cipher)
    print("Decrypted:", plain)

else:
    print("Invalid choice")




                 
