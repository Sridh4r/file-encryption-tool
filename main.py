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

# Create a key-value mapping using a dictionary. If no key is provided, generate one automatically.
def encrypt(key=None):
    value=string.ascii_letters+string.digits+string.punctuation+" "
    value_char=list(value)
    if not key:
        key=value_char.copy()
        random.shuffle(key)
    else:
        key=list(key)
    cipher_map ={}
    for i in range(len(value_char)):
        cipher_map [value_char[i]]=key[i]
    return cipher_map  , key

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

def validateFile(input_file,output_file):
    protected_file="encryption_key.txt"
    if input_file==protected_file or output_file==protected_file:
        print(f"Error: Direct operations on '{protected_file}' are not allowed ")
        return False
    elif input_file==output_file:
        choice=input("Both input file and output file are same this may cause OVERWRITE did you want to continue (Y/N): ").upper()
        if choice=="Y":
            return True
        elif choice=="N":
            return False
        else:
            print("Invalid choice ")
            return validateFile(input_file,output_file)
    return True

def encrypt_file(input_file,output_file,cipher_map):
    
    try:
        with open(input_file,"r",encoding='utf-8') as ip_file:
            message=ip_file.read()
        if not message:
            print("The message file is empty")
            return
        
        if not validateFile(input_file,output_file):
            return
        
        encrypted_message=encrypt_message(message,cipher_map)
    
        with open(output_file,"w",encoding='utf-8')as op_file:
            op_file.write(encrypted_message)
        print(f"The file {input_file} is Encrypted into {output_file} successfully")

    except FileNotFoundError:
        print("Input File not found")
    except Exception as e:
        print(f"Error occured {e}")



def decrypt_file(input_file,output_file,cipher_map):
    
    try:
        with open(input_file,"r",encoding='utf-8') as ip_file:
            encrypted_message=ip_file.read()
        if not encrypted_message:
            print("The encrypted file is empty")
            return
        if not validateFile(input_file,output_file):
            return
        message=decrypt_message(encrypted_message,cipher_map)

        with open(output_file,"w",encoding='utf-8')as op_file:
            op_file.write(message)
        print(f"The file {input_file} is Decrypted into {output_file} successfully")

    except FileNotFoundError:
        print("Input File not found")
    except Exception as e:
        print(f"Error occured: {e}")


# Controls the main program flow and handles errors like ValueError and invalid number selections.
def main():
    print("-"*50)
    print("- - - - - - - - Text Encryption- - - - - - - - ")
    print("-"*50)
    
    key=getKey()
       
    cipher_map,key=encrypt(key)
    while True:
        
        print("1 -> Encrypt a message\n2 -> Decrypt a message\n3 -> Encrypt a file\n4 -> Decrypt a file\n5 -> Update key\n6 -> Exit: ")
        n = input("What do you want to: ")
        print("-"*50)
        
        if n=="1":
            message=input("Enter your Message: ")
            print(f"Encrypted message is: {encrypt_message(message,cipher_map)}")
            
        elif n=="2":
            message=input("Enter your encrypted message: ")
            print(f"original message is: {decrypt_message(message,cipher_map)}")

        elif n=="3":
            input_file = input("Enter input file path (e.g., 'secret.txt'): ")
            output_file = input("Enter output file path (e.g., 'encrypted_secret.txt'): ")
            encrypt_file(input_file, output_file, cipher_map)
           
        elif n=="4":
            input_file = input("Enter input file path (e.g., 'encrypted_secret.txt'): ")
            output_file = input("Enter output file path (e.g., 'message.txt'): ")
            decrypt_file(input_file, output_file, cipher_map)
        
        elif n=="5":
            print("""Warning! \n this action will OVERWRITE "encryption_key.txt"\n Make sure to copy your key from "encryption_key.txt" before continuing \n or the encrypted file will be imposible to decode """)
            choice = input(" (Y -> continue)   (any other key -> stop): ").upper()
            if choice=="Y":
                cipher_map,key=encrypt()
                print("The key has been updated")
                with open("encryption_key.txt","w")as f:
                    f.write("".join(key))
            else:
                continue

        elif n=="6":
            with open("encryption_key.txt","w")as f:
                f.write("".join(key))
            print("""The key is saved in "encryption_key.txt" please avoid making any changes in the file""")
            break
            
        else:
            print("Please enter a valid input")
        print("-"*50)


if __name__=='__main__':
    main()