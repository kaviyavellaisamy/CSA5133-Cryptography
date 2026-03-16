import hashlib

def mac_generate(key, message, algo="sha256"):
    """Generate MAC using SHA family algorithms."""
    data = (key + message).encode()
    if algo == "sha1":
        return hashlib.sha1(data).hexdigest()
    elif algo == "sha256":
        return hashlib.sha256(data).hexdigest()
    elif algo == "sha512":
        return hashlib.sha512(data).hexdigest()
    else:
        raise ValueError("Unsupported algorithm! Choose sha1, sha256, or sha512.")

# --- Interactive Program ---
if __name__ == "__main__":
    print("=== MAC Generator (SHA) ===")
    key = input("Enter secret key: ")
    message = input("Enter message: ")
    algo = input("Choose hash algorithm (sha1 / sha256 / sha512): ").strip().lower()

    mac_value = mac_generate(key, message, algo)
    print("\nGenerated MAC:", mac_value)
