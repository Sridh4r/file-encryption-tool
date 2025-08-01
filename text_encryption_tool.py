import string
import random

def validKey(key):
    if not key:
        return key
    elif len(key)!=95 or len(set(key))!=95:
        print("Your key is invalid make sure it contain 95 unique characters")
        x=input("do you have a valid Key (Y/N) if no the program will produce a new key: ").upper()
        if x=='Y':
            key=input("Enter your valid key: ")
            return validKey(key)
        else:
            key=None
    return key


def printLine():
    print("-----------------------------------------------")

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

def encrypt_message(message,cipher_map):
    encrypted_message=""
    for ch in message:
        encrypted_message+=cipher_map[ch]
    return encrypted_message

def decrypt_message(message,cipher_map):
    map_inv={v:k for k , v in cipher_map.items()}
    original_message=""
    for ch in message:
        original_message+=map_inv[ch]
    return original_message



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