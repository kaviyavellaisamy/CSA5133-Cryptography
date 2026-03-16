import random

def generate_bits(n):
    """Generate n random bits (0 or 1)."""
    return [random.randint(0,1) for _ in range(n)]

def generate_bases(n):
    """Generate n random bases (0=rectilinear, 1=diagonal)."""
    return [random.randint(0,1) for _ in range(n)]

def measure(qubits, bases, chosen_bases):
    """Simulate measurement of qubits with chosen bases."""
    results = []
    for qbit, base, chosen in zip(qubits, bases, chosen_bases):
        if base == chosen:
            results.append(qbit)  # correct measurement
        else:
            results.append(random.randint(0,1))  # random outcome
    return results

def bb84_protocol(n=20):
    # Step 1: Alice generates random bits and bases
    alice_bits = generate_bits(n)
    alice_bases = generate_bases(n)

    # Step 2: Bob chooses random bases
    bob_bases = generate_bases(n)

    # Step 3: Bob measures qubits
    bob_results = measure(alice_bits, alice_bases, bob_bases)

    # Step 4: Alice and Bob compare bases (publicly)
    matching_indices = [i for i in range(n) if alice_bases[i] == bob_bases[i]]

    # Step 5: Shared key = bits where bases matched
    alice_key = [alice_bits[i] for i in matching_indices]
    bob_key   = [bob_results[i] for i in matching_indices]

    return alice_bits, alice_bases, bob_bases, bob_results, alice_key, bob_key


# Example run
if __name__ == "__main__":
    alice_bits, alice_bases, bob_bases, bob_results, alice_key, bob_key = bb84_protocol(20)

    print("Alice bits:   ", alice_bits)
    print("Alice bases:  ", alice_bases)
    print("Bob bases:    ", bob_bases)
    print("Bob results:  ", bob_results)
    print("Alice key:    ", alice_key)
    print("Bob key:      ", bob_key)
