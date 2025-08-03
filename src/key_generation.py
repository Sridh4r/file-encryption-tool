import string
import random

value=string.ascii_letters+string.digits+string.punctuation+" "

def create_key():
    key=list(value)
    random.shuffle(key)
    return "".join(key)

def validateKey(key):
    if not key:
        return key
    if len(key) != len(value) or set(key) != set(value):
        n=input("No valid key found if you want to try again press 1 or press 2 for new key: ")
        if n== "1":
            key=input("Enter your key: ")
            return validateKey(key)
        elif n=="2":
            print("new key generated")
            key=None
            return key
        else:
            print("Invalid input")
        return validateKey(key)
    else:
        return key



def getKey():
    choice=input("Do you want to enter the key manually? (Y/n): ").upper()
    if choice=="Y":
        key=input("Key: ")
        return validateKey(key)
    try:
        with open("encryption_key.txt","r") as f:
            key=f.read()
            return validateKey(key)
    except FileNotFoundError:
        n=input("No key found in your system. if you want enter it manually press 1 or press 2 for new key: ")
        if n=="1":
            key=input("Enter your Key: ")
            return validateKey(key)
        elif n=="2": 
            print("new key generated")
            key=None
            return key
        else:
            print("Invalid input")
    return validateKey(key)

def initialize_key(key=None):

    if not key:
        key=create_key()
    else:
        pass
    cipher_map ={}
    for i in range(len(value)):
        cipher_map [value[i]]=key[i]
    return cipher_map  , key


def save_key(key):
    with open("encryption_key.txt","w")as f:
        f.write(key)