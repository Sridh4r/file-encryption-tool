import string
import random

value=string.ascii_letters+string.digits+string.punctuation+" "

def create_key():
    key=list(value)
    random.shuffle(key)
    return "".join(key)


def validate_key(key):
    if not key:
        return False
    if len(key) != len(value) or set(key) != set(value):
        return False
    return True


def getKey():
    try:
        with open("encryption_key.txt","r") as f:
            key=f.read()
            return key
    except FileNotFoundError:
        n=input("No file found in your system. if you want enter it manually press 1 or press 2 for new key: ")
        if n=="1":
            key=input("Enter your Key: ")
            return key
        elif n=="2": 
            print("new key generated")
            key=None
            return key
        else:
            print("Invalid input")
    return key


def get_cipher_map(key):
    cipher_map ={}
    for i in range(len(value)):
        cipher_map [value[i]]=key[i]
    return cipher_map


def save_key(key):
    with open("encryption_key.txt","w")as f:
        f.write(key)