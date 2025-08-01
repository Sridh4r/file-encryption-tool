import string
import random

def validKey(key):
    if key==None or key=="":
        return True
    elif len(key)!=95:
        return False
    return True


def printLine():
    print("*************************")

def encrypt(key=None):
    value=string.ascii_letters+string.digits+string.punctuation+" "
    value_char=list(value)
    if key==None or key=="":
        key=value_char.copy()
        random.shuffle(key)
    else:
        key=list(key)
    
    map={}
    for i in range(len(value_char)):
        map[value_char[i]]=key[i]
    return map , key

def encrypt_message(message,map):
    encrypted_message=""
    for ch in message:
        encrypted_message+=map[ch]
    return encrypted_message

def decrypt_message(message,map):
    map_inv={v:k for k , v in map.items()}
    original_message=""
    for ch in message:
        original_message+=map_inv[ch]
    return original_message



def main():
    printLine()
    key=input("Enter your key if you don't have one press enter: ")
    if not validKey(key):
        x=int(input("The key you have been provided is not valid press 1 to create new one press 2 to exit: "))
        if x==1:
            key=None
        else:
            print("Program exit")
            printLine()
            return
       
    map,key=encrypt(key)
    while True:
        try:
            printLine()
            n = int(input("Whatdo you want to do with the meaage 1 -> encrypt  , 2 -> decrypt , 3 -> exit :"))
        except ValueError:
            print("Please enter a valid number (1, 2, or 3).")
            printLine()
            continue
        if n==1:
            message=input("Enter your Message: ")
            print(f"""Encrypted message is :"{encrypt_message(message,map)}" \ncopy for decryption""")
            
        elif n==2:
            message=input("Enter your Message: ")
            print(f"""original message is :"{decrypt_message(message,map)}" \ncopy for encryption""")
            

        elif n==3:
            print(f"""here is your key for future reference  '{''.join(key)}' Note the key did't include the first and last single quotes """)
            break
            
        else:
            print("Please enter a valid input")
            



if __name__=='__main__':
    main()