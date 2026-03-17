"""
The Vigenère Cipher is a polyalphabetic cipher that uses a keyword instead of a single shift.
Each letter in the key determines how much to shift:
Key repeats to match the message length
Each character is encrypted with a different shift

    Example
    Message: HELLO
    Key: KEY

H  E  L  L  O
K  E  Y  K  E
↓  ↓  ↓  ↓  ↓
R  I  J  V  S
"""

def generate_key(text, key):
    key = list(key)
    if len(text) == len(key):
        return key
    else:
        for i in range(len(text) - len(key)):
            key.append(key[i % len(key)])
    return "".join(key)


def vigenere_encrypt(text, key):
    key = generate_key(text, key)
    result = ""

    for i in range(len(text)):
        if text[i].isalpha():
            shift = ord(key[i].lower()) - 97
            base = 65 if text[i].isupper() else 97
            result += chr((ord(text[i]) - base + shift) % 26 + base)
        else:
            result += text[i]

    return result


def vigenere_decrypt(cipher, key):
    key = generate_key(cipher, key)
    result = ""

    for i in range(len(cipher)):
        if cipher[i].isalpha():
            shift = ord(key[i].lower()) - 97
            base = 65 if cipher[i].isupper() else 97
            result += chr((ord(cipher[i]) - base - shift) % 26 + base)
        else:
            result += cipher[i]

    return result


# 🔹 Example usage
message = input("Enter message: ")
key = input("Enter key: ")

encrypted = vigenere_encrypt(message, key)
print("Encrypted:", encrypted)

decrypted = vigenere_decrypt(encrypted, key)
print("Decrypted:", decrypted)