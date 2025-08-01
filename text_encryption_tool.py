import string
import random

# Keep prompting the user to enter a valid key until it's correct or they opt to exit
def validKey(key):
    if not key:
        return key
    elif len(key)!=95 or len(set(key))!=95 or set(key)!=set(string.ascii_letters+string.digits+string.punctuation+" "):
        print("Invalid key! Make sure it has exactly 95 unique ASCII characters (no emojis or missing symbols).")
        x=input("do you have a valid Key (Y/N) if no the program will produce a new key: ").upper()
        if x=='Y':
            key=input("Enter your valid key: ")
            return validKey(key)
        else:
            key=None
    return key


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
    key=input("Enter your key if you don't have one press enter: ")
    key=validKey(key)
        
       
    cipher_map,key=encrypt(key)
    while True:
        try:
            printLine()
            n = int(input("What do you want to do with the meaage 1 -> encrypt  , 2 -> decrypt , 3 -> exit: "))
        except ValueError:
            print("Please enter a valid number (1, 2, or 3).")
            continue
        if n==1:
            message=input("Enter your Message: ")
            print(f"Encrypted message is: {encrypt_message(message,cipher_map)}")
            
        elif n==2:
            message=input("Enter your decrypt message: ")
            print(f"original message is: {decrypt_message(message,cipher_map)}")
            

        elif n==3:
            print(f"here is your key for future reference:  {''.join(key)}")
            break
            
        else:
            print("Please enter a valid input")
            



if __name__=='__main__':
    main()