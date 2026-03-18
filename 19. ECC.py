from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric.utils import (
    encode_dss_signature, decode_dss_signature
)

# Generate ECC private key (using SECP256R1 curve)
private_key = ec.generate_private_key(ec.SECP256R1())

# Get the corresponding public key
public_key = private_key.public_key()

# Message to sign
message = b"Elliptic Curve Cryptography Example"

# Sign the message
signature = private_key.sign(
    message,
    ec.ECDSA(hashes.SHA256())
)

print("Signature:", signature)

# Verify the signature
try:
    public_key.verify(signature, message, ec.ECDSA(hashes.SHA256()))
    print("Signature is valid!")
except Exception as e:
    print("Signature verification failed:", e)