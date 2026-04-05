from Crypto.Util.Padding import unpad

# Helper tables for DES
IP = [
    58, 50, 42, 34, 26, 18, 10, 2,
    60, 52, 44, 36, 28, 20, 12, 4,
    62, 54, 46, 38, 30, 22, 14, 6,
    64, 56, 48, 40, 32, 24, 16, 8,
    57, 49, 41, 33, 25, 17, 9, 1,
    59, 51, 43, 35, 27, 19, 11, 3,
    61, 53, 45, 37, 29, 21, 13, 5,
    63, 55, 47, 39, 31, 23, 15, 7
]

FP = [
    40, 8, 48, 16, 56, 24, 64, 32,
    39, 7, 47, 15, 55, 23, 63, 31,
    38, 6, 46, 14, 54, 22, 62, 30,
    37, 5, 45, 13, 53, 21, 61, 29,
    36, 4, 44, 12, 52, 20, 60, 28,
    35, 3, 43, 11, 51, 19, 59, 27,
    34, 2, 42, 10, 50, 18, 58, 26,
    33, 1, 41, 9, 49, 17, 57, 25
]

E = [
    32, 1, 2, 3, 4, 5, 4, 5,
    6, 7, 8, 9, 8, 9, 10, 11,
    12, 13, 12, 13, 14, 15, 16, 17,
    16, 17, 18, 19, 20, 21, 20, 21,
    22, 23, 24, 25, 24, 25, 26, 27,
    28, 29, 28, 29, 30, 31, 32, 1
]

P = [
    16, 7, 20, 21, 29, 12, 28, 17,
    1, 15, 23, 26, 5, 18, 31, 10,
    2, 8, 24, 14, 32, 27, 3, 9,
    19, 13, 30, 6, 22, 11, 4, 25
]

S_BOX = [
    [[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
     [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
     [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
     [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]],

    [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
     [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
     [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
     [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]],

    [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
     [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
     [13, 6, 9, 0, 12, 11, 7, 3, 11, 1, 2, 12, 5, 10, 14, 7],
     [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]]
]

# Permute function
def permute(block, table):
    return ''.join(block[i - 1] for i in table)

# XOR operation
def xor(a, b):
    return ''.join(str(int(x) ^ int(y)) for x, y in zip(a, b))

# Feistel function for decryption
def feistel_decrypt(right, subkey):
    expanded = permute(right, E)
    xored = xor(expanded, subkey)
    substituted = ""
    for i in range(8):  # S-box substitution
        block = xored[i * 6:(i + 1) * 6]
        row = int(block[0] + block[-1], 2)
        col = int(block[1:5], 2)
        substituted += f"{S_BOX[i][row][col]:04b}"
    return permute(substituted, P)

# DES decryption for a single block
def des_decrypt_block(block, keys):
    block = permute(block, IP)
    left, right = block[:32], block[32:]
    for subkey in reversed(keys):
        new_right = xor(left, feistel_decrypt(right, subkey))
        left, right = right, new_right
    combined = right + left
    return permute(combined, FP)

# Key schedule generation (simplified)
def generate_keys(key):
    # Placeholder: Implement proper DES key schedule
    return [key[:48]] * 16

# Main DES decryption function
def des_decrypt(ciphertext, key):
    if len(key) != 8:
        raise ValueError("Key must be exactly 8 characters (64 bits).")
    binary_key = ''.join(f"{ord(c):08b}" for c in key)
    keys = generate_keys(binary_key)

    # Decrypt block by block
    decrypted_text = []
    for i in range(0, len(ciphertext), 64):  # 64-bit block size
        block = ciphertext[i:i + 64]
        decrypted_block = des_decrypt_block(block, keys)
        decrypted_text.append(decrypted_block)

    # Convert binary back to text
    decrypted_binary = ''.join(decrypted_text)
    decrypted_bytes = [int(decrypted_binary[i:i + 8], 2) for i in range(0, len(decrypted_binary), 8)]
    decrypted_plaintext = bytes(decrypted_bytes)
    return unpad(decrypted_plaintext, 8).decode()

if __name__ == "__main__":
    ciphertext = input("Enter ciphertext: ")
    key = input("Enter key (8 characters): ")

    try:
        plaintext = des_decrypt(ciphertext, key)
        print("Decrypted Plaintext:", plaintext)
    except ValueError as e:
        print("Error:", e)
