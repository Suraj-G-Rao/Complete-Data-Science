# Define the S-Boxes (the actual values for the S-boxes)
S_BOX = [
    [[14, 0, 11, 7, 1, 4, 13, 10, 9, 5, 0, 3, 8, 6, 15, 12], 
     [15, 10, 4, 1, 8, 14, 12, 11, 7, 13, 9, 6, 2, 5, 3, 0], 
     [4, 11, 12, 3, 1, 15, 13, 5, 8, 10, 6, 9, 0, 14, 7, 2], 
     [15, 9, 8, 0, 6, 3, 4, 14, 1, 13, 10, 11, 7, 5, 12, 2]],

    [[15, 1, 8, 14, 6, 11, 3, 10, 13, 4, 9, 7, 0, 5, 12, 2], 
     [1, 14, 8, 12, 4, 11, 9, 7, 5, 13, 0, 3, 15, 6, 10, 2], 
     [15, 6, 10, 1, 9, 8, 12, 7, 11, 14, 4, 3, 0, 5, 13, 2], 
     [8, 12, 10, 7, 5, 14, 6, 1, 13, 15, 0, 3, 9, 4, 11, 2]],

    [[15, 0, 5, 7, 11, 10, 8, 1, 6, 3, 9, 12, 13, 14, 4, 2], 
     [14, 10, 9, 15, 5, 6, 7, 12, 0, 11, 8, 1, 4, 2, 13, 3], 
     [9, 15, 8, 5, 14, 4, 11, 3, 7, 12, 1, 6, 2, 10, 0, 13], 
     [0, 4, 14, 7, 13, 1, 3, 9, 12, 6, 5, 15, 8, 10, 11, 2]],

    [[15, 5, 3, 8, 10, 14, 7, 13, 9, 4, 6, 11, 2, 12, 1, 0], 
     [12, 6, 7, 14, 8, 10, 1, 11, 9, 15, 13, 2, 5, 0, 3, 4], 
     [11, 12, 10, 14, 9, 4, 7, 15, 13, 6, 1, 3, 0, 5, 8, 2], 
     [3, 13, 15, 7, 4, 5, 2, 14, 8, 10, 12, 9, 1, 6, 0, 11]],

    [[15, 6, 8, 1, 3, 14, 11, 5, 0, 7, 12, 9, 10, 4, 13, 2], 
     [12, 15, 0, 5, 11, 3, 9, 10, 7, 8, 4, 6, 1, 2, 13, 14], 
     [5, 11, 13, 8, 12, 1, 14, 6, 9, 4, 7, 2, 10, 15, 3, 0], 
     [14, 7, 10, 2, 0, 4, 1, 9, 3, 12, 15, 11, 8, 5, 6, 13]],

    [[15, 10, 0, 9, 12, 4, 1, 3, 11, 7, 2, 5, 14, 13, 8, 6], 
     [14, 15, 11, 0, 6, 7, 9, 4, 3, 8, 12, 13, 1, 10, 5, 2], 
     [7, 15, 12, 3, 5, 0, 1, 4, 14, 6, 13, 9, 8, 11, 10, 2], 
     [9, 12, 10, 14, 15, 2, 1, 8, 7, 0, 5, 13, 3, 4, 6, 11]],

    [[15, 4, 7, 3, 0, 9, 1, 10, 11, 14, 8, 13, 5, 12, 2, 6], 
     [0, 3, 7, 13, 9, 5, 12, 11, 8, 14, 2, 15, 1, 10, 4, 6], 
     [14, 13, 8, 0, 12, 1, 3, 10, 4, 5, 15, 7, 9, 2, 11, 6], 
     [3, 4, 10, 12, 8, 2, 9, 7, 6, 0, 13, 15, 11, 14, 5, 1]],

    [[15, 13, 9, 6, 8, 4, 3, 12, 1, 11, 14, 10, 7, 0, 5, 2], 
     [4, 6, 10, 11, 15, 12, 7, 13, 8, 2, 9, 5, 1, 14, 3, 0], 
     [11, 1, 7, 10, 9, 13, 8, 12, 6, 0, 2, 3, 4, 14, 5, 15], 
     [7, 10, 5, 12, 3, 14, 1, 0, 9, 13, 6, 4, 8, 11, 15, 2]]
]

# Key schedule (for simplicity, this is a mockup for demonstration)
def key_schedule(key):
    # Example: return dummy 16 subkeys for demonstration purposes
    return ['0' * 48] * 16  # Normally, you'd expand the key properly here

# XOR operation
def xor(bits1, bits2):
    return ''.join('1' if b1 != b2 else '0' for b1, b2 in zip(bits1, bits2))

# Feistel function (f)
def feistel(right, subkey):
    if len(right) != 48:
        raise ValueError(f"Expected 48-bit block, but got {len(right)}-bit block.")
    
    # Split the 48-bit right block into 8 blocks of 6 bits
    blocks = [right[i:i+6] for i in range(0, 48, 6)]
    substituted = ''
    
    for i, block in enumerate(blocks):
        row = int(block[0] + block[5], 2)
        col = int(block[1:5], 2)
        print(f"S-Box {i}: block={block}, row={row}, col={col}")
        substituted += f"{S_BOX[i][row][col]:04b}"
    
    return substituted

# DES decryption block
def des_decrypt_block(block, keys):
    # Initial permutation (simplified, normally would be a permutation)
    left, right = block[:32], block[32:]

    # 16 rounds of decryption
    for i in range(15, -1, -1):
        subkey = keys[i]
        new_right = xor(left, feistel(right, subkey))
        left, right = right, new_right
    
    # Final permutation (simplified)
    return left + right

# DES decryption
def des_decrypt(ciphertext, key):
    keys = key_schedule(key)
    decrypted_text = ''

    # Split ciphertext into 64-bit blocks
    for i in range(0, len(ciphertext), 64):
        block = ciphertext[i:i+64]
        decrypted_block = des_decrypt_block(block, keys)
        decrypted_text += decrypted_block
    
    return decrypted_text

# Main program
if __name__ == '__main__':
    ciphertext = input("Enter ciphertext: ")
    key = input("Enter key (8 characters): ")
    decrypted_plaintext = des_decrypt(ciphertext, key)
    print("Decrypted plaintext:", decrypted_plaintext)
