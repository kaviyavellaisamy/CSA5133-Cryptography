import hmac
import hashlib

def hmac_generate(key, message, algo="sha256"):
    """Generate HMAC using the chosen algorithm."""
    if algo.lower() == "sha1":
        digestmod = hashlib.sha1
    elif algo.lower() == "sha256":
        digestmod = hashlib.sha256
    elif algo.lower() == "md5":
        digestmod = hashlib.md5
    else:
        raise ValueError("Unsupported algorithm! Choose sha1, sha256, or md5.")
    
    return hmac.new(key.encode(), message.encode(), digestmod).hexdigest()


# --- Interactive Program ---
if __name__ == "__main__":
    print("=== HMAC Generator ===")
    key = input("Enter secret key: ")
    message = input("Enter message: ")
    algo = input("Choose hash algorithm (sha1 / sha256 / md5): ").strip().lower()

    hmac_value = hmac_generate(key, message, algo)
    print("\nGenerated HMAC:", hmac_value)
