# 3301-atbash
A simple Python script that encodes or decodes messages via Atbash.

# Requirements
This script requires Python 3.6 or higher. No additional libraries need to be installed.

# How To Run
1. **Open a terminal**
- On *Windows*, press *Win + R*, then type *"cmd"* and hit *Enter*.
- On Mac/Linux, open the Terminal application.

2. **Navigate to the script's directory, e.g. where you saved it.**
- If the file *atbash.py* is located on your desktop, type the following command:
```
cd %UserProfile%\Desktop
```

3. **Run the script.**
```
python atbash.py
```

# Usage
1. Run the script (for a detailed guide on how to do this, check **How To Run** above).
2. You will be prompted to enter text. Once you type it out, it will ask if you want to Encrypt (type 'E') or Decrypt (type 'D').
3. The program exits itself automatically and you will have to run it again for repeated use.

# Examples
### Example 1: Encrypting text.
```
Enter the text you want to encrypt/decrypt: Example
Would you like to (E)ncrypt or (D)ecrypt?: E
Result: Vcznkov
```

### Example 2: Decrypting text.
```
Enter the text you want to encrypt/decrypt: Vcznkov
Would you like to (E)ncrypt or (D)ecrypt?: D
Result: Example
```

Please note that since Atbash only encodes letters (and this script only specifically the English alphabet), any number or special character will be returned as is.

# Explanation
- *atbash_cipher(text)* transforms the input text using the Atbash cipher and *result[]* stores the conversion.
- Everything in *for char in text* handles special characters, lowercase or uppercase.
- *25 - (ord(char) - 65)* finds the mirrored letter's position & *chr(65 + new_position)* converts the new position back to the character.

# Short FAQ For Newbies

### What Is Cicada 3301, Liber Primus, etc?
Cicada 3301 is a mysterious group that became known for posting complex puzzles online, starting in 2012. These puzzles challenged participants with cryptography & steganography. The group's ultimate purpose remains unclear, but as mentioned in the beginning of each puzzle, they are looking for "highly intelligent individuals".

You can read more about Cicada 3301 on [The Uncovering Cicada Fandom](https://uncovering-cicada.fandom.com/wiki/Uncovering_Cicada_Wiki), which also includes attempts at solving Liber Primus, Cicada's latest unresolved puzzle from 2014.

### What Is Atbash?
Atbash cipher is a simple monoalphabetic substitution cipher where each letter is replaced with its reverse counterpart in the alphabet. It was originally used in Hebrew, and some segments of the Bible are also encrypted via Atbash. Since the cipher is symmetric, the encryption and decryption work on the same basis and Atbash is not secure by modern standards.
