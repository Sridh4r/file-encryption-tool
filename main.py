import key_generation as k
import encryption as enc
import file_initializer as fi


def main():
    print("-"*50)
    print("- - - - - - - - Text Encryption- - - - - - - - ")
    print("-"*50)
    
    key=k.getKey()
       
    cipher_map,key=k.initialize_key(key)
    while True:
        
        print("1 -> Encrypt a message\n2 -> Decrypt a message\n3 -> Encrypt a file\n4 -> Decrypt a file\n5 -> Update key\n6 -> Exit: ")
        n = input("What do you want to: ").strip()
        print("-"*50)
        
        if n=="1":
            message=input("Enter your Message: ")
            print(f"Encrypted message is: {enc.encrypt_message(message,cipher_map)}")
            
        elif n=="2":
            message=input("Enter your encrypted message: ")
            print(f"original message is: {enc.decrypt_message(message,cipher_map)}")

        elif n=="3":
            print("\nNote:\nYou can perform in-place encryption/decryption by entering the same file name for input and output. ")

            input_file = input("Enter input file path (e.g., 'secret.txt'): ")
            output_file = input("Enter output file path (e.g., 'encrypted_secret.txt'): ")
            fi.encrypt_file(input_file, output_file, cipher_map)
           
        elif n=="4":
            print("\nNote:\nYou can perform in-place encryption/decryption by entering the same file name for input and output. ")
            input_file = input("Enter input file path (e.g., 'encrypted_secret.txt'): ")
            output_file = input("Enter output file path (e.g., 'message.txt'): ")
            fi.decrypt_file(input_file, output_file, cipher_map)
        
        elif n=="5":
            print("""Warning! \n this action will OVERWRITE "encryption_key.txt"\n Make sure to copy your key from "encryption_key.txt" before continuing \n or the encrypted file will be imposible to decode """)
            choice = input(" (Y -> continue or any other key -> stop): ").upper()
            if choice=="Y":
                cipher_map,key=k.initialize_key()
                print("The key has been updated")
                k.save_key(key)
                print("New key saved to 'encryption_key.txt'.")
            else:
                continue

        elif n=="6":
            k.save_key(key)
            print("""The key is saved in "encryption_key.txt" please avoid making any changes in the file""")
            break
            
        else:
            print("Please enter a valid input")
        print("-"*50)


if __name__=='__main__':
    main()