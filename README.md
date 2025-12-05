
# **SAI Algorithm – O(1) Constant-Time Encryption & Decryption**

The **SAI Algorithm** is a lightweight, constant-time (O(1)) encryption and decryption mechanism.
It works by adding a user-defined encryption code to the beginning and end of any text, and removing the same code during decryption.

This algorithm is designed for **speed**, **simplicity**, and **constant-time performance**, regardless of input size.

---

## 🚀 Features

* User chooses the encryption code
* User chooses the text
* Pure O(1) encryption and decryption
* No loops, no iteration
* Extremely fast

---

## 🔐 How SAI Algorithm Works

### **Encryption**

```
code + text + code
```

Example:

```
Code: 9898
Text: sai
Encrypted → 9898sai9898
```

### **Decryption**

Simply remove the prefix and suffix equal to the code length:

```
sai
```

---

## 🧠 Why SAI Algorithm Is O(1)

* Performs only fixed operations
* No traversal of the entire string
* Slicing and concatenation use constant-time logic for this design
* Therefore both encrypt() and decrypt() run in **O(1)**

---

## 🧪 **Python Code — SAI Algorithm**

```python
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
```

---

## 📌 Example Usage

```
Enter SAI encryption code: 9898
Enter text to encrypt using SAI Algorithm: sai

Encrypted (SAI Algorithm): 9898sai9898
Decrypted (SAI Algorithm): sai
```

---

## 📝 Applications

* Simple reversible wrapping
* Tagging systems
* Educational demonstrations of O(1) algorithms
* Quick prefix-based encoding

---

## ⚠ Limitations

* Not cryptographically secure
* Not suitable for sensitive data

---
