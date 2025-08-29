#!/u# Caesar Cipher Program

def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():  # Encrypt only letters
            shift_base = 65 if char.isupper() else 97
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result


def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)


# Main program
if __name__ == "__main__":
    message = input("Enter your message: ")
    shift = int(input("Enter shift value: "))
    
    encrypted_text = caesar_encrypt(message, shift)
    print(f"\nEncrypted Message: {encrypted_text}")
    
    decrypted_text = caesar_decrypt(encrypted_text, shift)
    print(f"Decrypted Message: {decrypted_text}");str/bin/python3
import time
 
t = time.localtime(time.time())
localtime = time.asctime(t)
str = "Current Time:" + time.asctime(t)
 
print(str)