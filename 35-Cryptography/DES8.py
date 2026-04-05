from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
import binascii

# Function to perform DES encryption and decryption
def des_decrypt(ciphertext, key):
    # Convert the key to bytes
    key_bytes = key.encode('utf-8')
    
    # Create a DES cipher object
    cipher = DES.new(key_bytes, DES.MODE_ECB)
    
    # Decrypt the ciphertext (decode from binary string to bytes)
    ciphertext_bytes = binascii.unhexlify(ciphertext)
    
    # Decrypt using DES
    decrypted_data = cipher.decrypt(ciphertext_bytes)
    
    # Unpad the decrypted data
    decrypted_data = unpad(decrypted_data, DES.block_size)
    
    return decrypted_data.decode('utf-8')

# Example function to display encryption and decryption with default values
def main():
    # Given ciphertext in hex format
    ciphertext = "101011111011000110111010100010100001110100001011111111010111000010100111011010110111101110101001001011111110011110001101111111101001100001010011110110100100110100011111100000010001100110001111"
    
    # Convert the binary ciphertext to hex
    ciphertext_hex = bin(int(ciphertext, 2))[2:].zfill(len(ciphertext) // 4)
    
    # Key for DES
    key = "12345678"
    
    # Decrypt the ciphertext
    decrypted_text = des_decrypt(ciphertext_hex, key)
    
    # Print the decrypted result
    print(f"Ciphertext: {ciphertext}")
    print(f"Decrypted text: {decrypted_text}")

if __name__ == "__main__":
    main()
