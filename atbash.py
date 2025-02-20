def atbash_cipher(text):
    result = []
    
    for char in text:
        if char.isupper():
            result.append(chr(65 + (25 - (ord(char) - 65))))
        elif char.islower():
            result.append(chr(97 + (25 - (ord(char) - 97))))
        else:
            result.append(char)
    return ''.join(result)

def main():
    text = input("Enter the text you want to encrypt/decrypt: ")
    choice = input("Would you like to (E)ncrypt or (D)ecrypt?: ").lower()

    if choice == 'e' or choice == 'd':
        result = atbash_cipher(text)
        print(f"Result: {result}")
    else:
        print("Invalid choice. Please select 'E' for encryption or 'D' for decryption.")

if __name__ == "__main__":
    main()
