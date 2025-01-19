# Caesar Cipher Encryption and Decryption

def caesar_cipher(text, shift, mode="encrypt"):
    result = ""
    if mode == "decrypt":
        shift = -shift

    for char in text:
        if char.isalpha():
            # Handle both uppercase and lowercase letters
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            # Non-alphabetic characters remain unchanged
            result += char

    return result

# User interaction
def main():
    print("\nWelcome to the Caesar Cipher Program!")
    print("This program lets you encrypt or decrypt messages using a Caesar cipher.\n")
    while True:
        print("Options:")
        print("  e: Encrypt a message")
        print("  d: Decrypt a message")
        print("  q: Quit the program")
        choice = input("\nEnter your choice (e/d/q): ").strip().lower()

        if choice == 'q':
            print("\nThank you for using the Caesar Cipher Program. Goodbye!")
            break
        elif choice in ['e', 'd']:
            text = input("\nEnter your message: ").strip()
            try:
                shift = int(input("Enter the shift value (integer): ").strip())
            except ValueError:
                print("\nError: Please enter a valid integer for the shift value.")
                continue

            mode = "encrypt" if choice == 'e' else "decrypt"
            result = caesar_cipher(text, shift, mode)
            print(f"\nResult ({'Encrypted' if mode == 'encrypt' else 'Decrypted'}): {result}\n")
        else:
            print("\nInvalid choice. Please select 'e', 'd', or 'q'.\n")

if __name__ == "__main__":
    main()

