print("------- Welcome to SAI Encryption & Decryption Algorithm -----------")


def sai_encrypt(text, code):
    return code + text + code

def sai_decrypt(cipher, code):
    l = len(code)
    return cipher[l:-l]

code = input("Enter SAI encryption code: ")
text = input("Enter text to encrypt using SAI Algorithm: ")

encrypted = sai_encrypt(text, code)
print("Encrypted (SAI Algorithm):", encrypted)

decrypted = sai_decrypt(encrypted, code)
print("Decrypted (SAI Algorithm):", decrypted)
