def encrypt(text):
    encrypted_text = []
    for char in text:
        if char.isalpha():  
            shifted_char = chr((ord(char.lower()) - ord('a') + 3) % 26 + ord('a'))
            encrypted_text.append(shifted_char.upper() if char.isupper() else shifted_char)
        elif char.isdigit():  
            new_digit = str(9 - int(char))
            encrypted_text.append(new_digit)
        elif char == '.':
            encrypted_text.append(',')
        elif char == ',':
            encrypted_text.append('.')
        else:
            encrypted_text.append(char)
    return ''.join(encrypted_text)

def decrypt(text):
    decrypted_text = []
    for char in text:
        if char.isalpha(): 
            shifted_char = chr((ord(char.lower()) - ord('a') - 3) % 26 + ord('a'))
            decrypted_text.append(shifted_char.upper() if char.isupper() else shifted_char)
        elif char.isdigit(): 
            new_digit = str(9 - int(char))
            decrypted_text.append(new_digit)
        elif char == '.':
            decrypted_text.append(',')
        elif char == ',':
            decrypted_text.append('.')
        else:
            decrypted_text.append(char)
    return ''.join(decrypted_text)

mensagem_original = "Hello, World! 123."
mensagem_criptografada = encrypt(mensagem_original)
mensagem_descriptografada = decrypt(mensagem_criptografada)

print("Mensagem Original:", mensagem_original)
print("Mensagem Criptografada:", mensagem_criptografada)
print("Mensagem Descriptografada:", mensagem_descriptografada)
