import string
import random

# Validates a substitution key; prompts to retry or generate a new one if invalid
def validateKey(key):
    if not key:
        return key
    if len(key)!=95 or len(set(key))!=95 or set(key)!=set(string.ascii_letters+string.digits+string.punctuation+" "):
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

# Retrieves the encryption key from file or prompts user to enter/generate one
def getKey():
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


 # Print a horizontal line to separate output sections
def printLine():
    print("-----------------------------------------------")

# Create a key-value mapping using a dictionary. If no key is provided, generate one automatically.
def encrypt(key=None):
    value=string.ascii_letters+string.digits+string.punctuation+" "
    value_char=list(value)
    if not key:
        key=value_char.copy()
        random.shuffle(key)
    else:
        key=list(key)
    map={}
    for i in range(len(value_char)):
        map[value_char[i]]=key[i]
    return map , key

# Encrypt the message by replacing each character with its corresponding value from the key mapping.
def encrypt_message(message,cipher_map):
    encrypted_message=""
    for ch in message:
        encrypted_message+=cipher_map[ch]
    return encrypted_message

# Decrypt the message by reversing the key-value pairs from the original dictionary and mapping each character accordingly.

def decrypt_message(message,cipher_map):
    map_inv={v:k for k , v in cipher_map.items()}
    original_message=""
    for ch in message:
        original_message+=map_inv[ch]
    return original_message


# Controls the main program flow and handles errors like ValueError and invalid number selections.
def main():
    printLine()
    print("- - - - - - - - Text Encryption- - - - - - - - ")
    printLine()
    
    key=getKey()
       
    cipher_map,key=encrypt(key)
    while True:
        try:
            printLine()
            n = int(input("What do you want to do with the message 1 -> encrypt, 2 -> decrypt, 3 -> exit: "))

        except ValueError:
            print("Please enter a valid number (1, 2, or 3).")
            continue
        if n==1:
            message=input("Enter your Message: ")
            print(f"Encrypted message is: {encrypt_message(message,cipher_map)}")
            
        elif n==2:
            message=input("Enter your encrypted message: ")
            print(f"original message is: {decrypt_message(message,cipher_map)}")
            

        elif n==3:
            with open("encryption_key.txt","w")as f:
                f.write("".join(key))
            print("""The key is saved in "encryption_key.txt" please avoid making any changes in the file""")
            break
            
        else:
            print("Please enter a valid input")
            


if __name__=='__main__':
    main()