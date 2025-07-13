import base64

def encrypt_text(text):
    encrypted = ''
    for char in text:
        encrypted += chr(255 - ord(char))
    # Convert to bytes and then Base64 encode for readability
    return base64.b64encode(encrypted.encode()).decode()

def decrypt_text(encrypted_text):
    try:
        # Decode from Base64 and reverse the encryption
        encrypted_bytes = base64.b64decode(encrypted_text.encode())
        decrypted = ''
        for char in encrypted_bytes.decode():
            decrypted += chr(255 - ord(char))
        return decrypted
    except Exception as e:
        return f"Decryption failed: {str(e)}"

# Menu
def main():
    while True:
        print("\n=== Prodigy - Text Encryptor ===")
        print("1. Encrypt Text")
        print("2. Decrypt Text")
        print("3. Exit")

        choice = input("\nEnter your choice (1/2/3): ")

        if choice == '1':
            text = input("Enter text to encrypt: ")
            encrypted = encrypt_text(text)
            print(f"\nEncrypted: {encrypted}")

        elif choice == '2':
            encrypted_text = input("Enter encrypted text: ")
            decrypted = decrypt_text(encrypted_text)
            print(f"\nDecrypted: {decrypted}")

        elif choice == '3':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
