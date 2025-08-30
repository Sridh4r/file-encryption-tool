import src.key_generation as k
import src.encryption as enc


key=""
clipper_map=""
def get_key():
    return k.getKey()

def valid_key(key):
    return k.validate_key(key)

def encrypt(message):
    return enc.encrypt_message(message,k.get_cipher_map(key))

def decrypt(encrypted_message):
    return enc.decrypt_message(encrypted_message,k.get_cipher_map(key))


def generate_key():
    key=k.create_key()
    return key

def save_key(new_key):
    global key
    key=new_key