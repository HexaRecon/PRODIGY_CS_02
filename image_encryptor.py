import cv2
import numpy as np
import os

def encrypt_image(input_path, output_path):
    img = cv2.imread(input_path)
    if img is None:
        print("Error: Image not found.")
        return

    # Invert colors (255 - pixel) and flip horizontally
    encrypted_img = 255 - img
    encrypted_img = cv2.flip(encrypted_img, 1)  # 1 = horizontal flip

    cv2.imwrite(output_path, encrypted_img)
    print(f"[✔] Encrypted image saved to: {output_path}")


def decrypt_image(input_path, output_path):
    img = cv2.imread(input_path)
    if img is None:
        print("Error: Encrypted image not found.")
        return

    # Reverse the encryption process
    decrypted_img = cv2.flip(img, 1)
    decrypted_img = 255 - decrypted_img

    cv2.imwrite(output_path, decrypted_img)
    print(f"[✔] Decrypted image saved to: {output_path}")


def main():
    print("\n=== Prodigy - Image Encryptor ===")
    print("1. Encrypt Image")
    print("2. Decrypt Image")
    print("3. Exit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        input_path = input("Enter path to image to encrypt (e.g., input.png): ")
        output_path = "encrypted.png"
        encrypt_image(input_path, output_path)

    elif choice == '2':
        input_path = input("Enter path to encrypted image (e.g., encrypted.png): ")
        output_path = "decrypted.png"
        decrypt_image(input_path, output_path)

    elif choice == '3':
        print("Goodbye!")
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
