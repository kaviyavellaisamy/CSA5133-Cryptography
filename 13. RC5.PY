import struct

class RC5:
    def __init__(self, key, w=32, r=12):
        self.w, self.r, self.mod = w, r, 2**w
        self.P, self.Q = 0xB7E15163, 0x9E3779B9
        self.S = self.expand_key(key)

    def rol(self, x, y): return ((x << (y & (self.w-1))) | (x >> (self.w-(y & (self.w-1))))) % self.mod
    def ror(self, x, y): return ((x >> (y & (self.w-1))) | (x << (self.w-(y & (self.w-1))))) % self.mod

    def expand_key(self, key):
        u, b = self.w//8, len(key)
        L = [0]*(b//u)
        for i in range(b-1, -1, -1): L[i//u] = (L[i//u]<<8)+key[i]
        S = [(self.P + i*self.Q) % self.mod for i in range(2*(self.r+1))]
        A=B=i=j=0
        for _ in range(3*max(len(S), len(L))):
            A = S[i] = self.rol((S[i]+A+B)%self.mod, 3)
            B = L[j] = self.rol((L[j]+A+B)%self.mod, (A+B))
            i, j = (i+1)%len(S), (j+1)%len(L)
        return S

    def encrypt_block(self, block):
        A,B = struct.unpack('<2I', block)
        A, B = (A+self.S[0])%self.mod, (B+self.S[1])%self.mod
        for i in range(1, self.r+1):
            A = (self.rol(A^B, B)+self.S[2*i])%self.mod
            B = (self.rol(B^A, A)+self.S[2*i+1])%self.mod
        return struct.pack('<2I', A, B)

    def decrypt_block(self, block):
        A,B = struct.unpack('<2I', block)
        for i in range(self.r,0,-1):
            B = self.ror((B-self.S[2*i+1])%self.mod, A)^A
            A = self.ror((A-self.S[2*i])%self.mod, B)^B
        return struct.pack('<2I', (A-self.S[0])%self.mod, (B-self.S[1])%self.mod)

    # --- Utility for arbitrary length ---
    def pad(self, data):
        pad_len = 8 - (len(data) % 8)
        return data + bytes([pad_len])*pad_len

    def unpad(self, data):
        pad_len = data[-1]
        return data[:-pad_len]

    def encrypt(self, data):
        data = self.pad(data)
        blocks = [data[i:i+8] for i in range(0, len(data), 8)]
        return b"".join(self.encrypt_block(b) for b in blocks)

    def decrypt(self, data):
        blocks = [data[i:i+8] for i in range(0, len(data), 8)]
        plain = b"".join(self.decrypt_block(b) for b in blocks)
        return self.unpad(plain)


# --- Interactive Program ---
if __name__ == "__main__":
    key = input("Enter secret key: ").encode()
    rc5 = RC5(key)

    choice = input("Choose (E)ncrypt or (D)ecrypt: ").strip().upper()

    if choice == "E":
        text = input("Enter plaintext: ").encode()
        ciphertext = rc5.encrypt(text)
        print("Ciphertext (hex):", ciphertext.hex())

    elif choice == "D":
        hex_text = input("Enter ciphertext (hex): ").strip()
        ciphertext = bytes.fromhex(hex_text)
        plaintext = rc5.decrypt(ciphertext)
        print("Decrypted text:", plaintext.decode(errors="ignore"))

    else:
        print("Invalid choice! Please select E or D.")
