
# Encrypt the message by replacing each character with its corresponding value from the key mapping.
def encrypt_message(message,cipher_map):
    encrypted_message=""
    for ch in message:
        if ch not in cipher_map:
            encrypted_message+=ch
            continue
        encrypted_message+=cipher_map[ch]
    return encrypted_message

# Decrypt the message by reversing the key-value pairs from the original dictionary and mapping each character accordingly.

def decrypt_message(message,cipher_map):
    map_inv={v:k for k , v in cipher_map.items()}
    original_message=""
    for ch in message:
        if ch not in cipher_map:
            original_message+=ch
            continue
        original_message+=map_inv[ch]
    return original_message
