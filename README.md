# FortFile - A Simple Text Encryption Tool

FortFile is a web-based tool for encrypting and decrypting text files using a simple substitution cipher. It's designed as an educational project to demonstrate the basic principles of web applications and encryption.

**⚠️ Important Security Disclaimer**
This tool is for **educational and demonstrational purposes only**. The substitution cipher used is **not secure** and can be easily broken. **Do not use this tool to protect sensitive or private data.** For real-world security, please use industry-standard encryption tools like VeraCrypt, GPG, or BitLocker.

## Features

-   **Encrypt Files**: Upload a text file to encrypt its contents.
-   **Decrypt Files**: Upload an encrypted file and the corresponding key to get the original message.
-   **Key Management**:
    -   Generate a new random key.
    -   Upload an existing key file.
    -   Download the current key.
-   **Web-Based Interface**: Easy-to-use interface built with Flask.

## Getting Started

### Prerequisites

-   Python 3.x
-   Flask

### Installation & Running Locally

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Sridh4r/text-encryption-tool.git
    cd text-encryption-tool
    ```

2.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the application:**
    ```bash
    python app.py
    ```

4.  Open your web browser and navigate to `http://127.0.0.1:5000`.

## Project Structure

## How It Works

The application uses a simple substitution cipher where each character is mapped to another character based on a randomly generated key. The key file contains this mapping.

-   **Encryption**: Replaces each character in the input file with its corresponding character from the key.
-   **Decryption**: Replaces each character in the encrypted file with its original character using the key.



## License
This project is licensed under the [MIT License](LICENSE).