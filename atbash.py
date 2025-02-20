# Atbash Cipher Implementation

# Function to perform Atbash cipher encryption or decryption
def atbash_cipher(text):
    result = []
    
    for char in text:
        # Check if the character is an uppercase letter
        if char.isupper():
            result.append(chr(65 + (25 - (ord(char) - 65))))
        # Check if the character is a lowercase letter
        elif char.islower():
            result.append(chr(97 + (25 - (ord(char) - 97))))
        else:
            # Non-alphabet characters remain the same
            result.append(char)
    
    return ''.join(result)

def main():
    # Get input from the user
    text = input("Enter the text you want to encrypt/decrypt: ")
    
    # Ask the user for operation: encryption or decryption
    choice = input("Would you like to (E)ncrypt or (D)ecrypt?: ").lower()

    if choice == 'e' or choice == 'd':
        # Perform encryption or decryption (they are the same in Atbash)
        result = atbash_cipher(text)
        print(f"Result: {result}")
    else:
        print("Invalid choice. Please select 'E' for encryption or 'D' for decryption.")

if __name__ == "__main__":
    main()
