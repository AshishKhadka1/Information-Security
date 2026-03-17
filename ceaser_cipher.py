"""" 
A simple encryption technique where each letter is shifted by a fixed number.

Example (shift = 3):
A → D
B → E
X → A 
"""

def caesar_encrypt(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char

    return result


def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)


# 🔹 Example usage
message = input("Enter message: ")
shift = int(input("Enter shift value: "))

encrypted = caesar_encrypt(message, shift)
print("Encrypted:", encrypted)

decrypted = caesar_decrypt(encrypted, shift)
print("Decrypted:", decrypted)