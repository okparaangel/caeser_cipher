# Create a caesar cipher that encripts and decripts user input using brut force






def caesar_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            encrypted_text += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
        else:
            encrypted_text += char
    return encrypted_text
def caesar_decrypt(encrypted_text, shift):
    return caesar_encrypt(encrypted_text, -shift)
def caesar_brute_force(encrypted_text):
    for shift in range(26):
        decrypted_text = caesar_decrypt(encrypted_text, shift)
        print(f"Shift {shift}: {decrypted_text}")
def main():
    choice = input("Enter 'e' to encrypt, 'd' to decrypt, or 'b' for brute-force decryption: ")
    if choice.lower() == 'e':
        plaintext = input("Enter text to encrypt: ")
        shift = int(input("Enter the shift value: "))
        encrypted_text = caesar_encrypt(plaintext, shift)
        print("Encrypted:", encrypted_text)
    elif choice.lower() == 'd':
        encrypted_text = input("Enter text to decrypt: ")
        shift = int(input("Enter the shift value: "))
        decrypted_text = caesar_decrypt(encrypted_text, shift)
        print("Decrypted:", decrypted_text)
    elif choice.lower() == 'b':
        encrypted_text = input("Enter text to decrypt using brute force: ")
        caesar_brute_force(encrypted_text)
    else:
        print("Invalid choice")
if __name__ == "__main__":
    main()
