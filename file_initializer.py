import encryption as enc
    
def validateFile(input_file,output_file):
    protected_file="encryption_key.txt"
    if input_file==protected_file or output_file==protected_file:
        print(f"Error: Direct operations on '{protected_file}' are not allowed ")
        return False
    elif input_file==output_file:
        choice = input("You are performing an in-place operation. This will OVERWRITE the original file.\nDo you want to continue? (Y/N): ").strip().upper()
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
        
        encrypted_message=enc.encrypt_message(message,cipher_map)
    
        with open(output_file,"w",encoding='utf-8')as op_file:
            op_file.write(encrypted_message)
        print(f"The file {input_file} is Encrypted into {output_file} successfully")

    except FileNotFoundError:
        print("Input File not found")
    except Exception as E:
        print(f"Error occured: {E}")



def decrypt_file(input_file,output_file,cipher_map):
    
    try:
        with open(input_file,"r",encoding='utf-8') as ip_file:
            encrypted_message=ip_file.read()
        if not encrypted_message:
            print("The encrypted file is empty")
            return
        if not validateFile(input_file,output_file):
            return
        message=enc.decrypt_message(encrypted_message,cipher_map)

        with open(output_file,"w",encoding='utf-8')as op_file:
            op_file.write(message)
        print(f"The file {input_file} is Decrypted into {output_file} successfully")

    except FileNotFoundError:
        print("Input File not found")
    except Exception as E:
        print(f"Error occured: {E}")